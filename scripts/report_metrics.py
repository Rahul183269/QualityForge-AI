
import xml.etree.ElementTree as ET
from pathlib import Path


def calculate_metrics(report_path):
    path = Path(report_path)

    if not path.exists():
        raise FileNotFoundError(f"Report not found: {path}")

    root = ET.parse(path).getroot()

    if root.tag == "testsuite":
        suites = [root]
    else:
        suites = root.findall(".//testsuite")

    total = sum(int(s.get("tests", 0)) for s in suites)
    failures = sum(int(s.get("failures", 0)) for s in suites)
    errors = sum(int(s.get("errors", 0)) for s in suites)
    skipped = sum(int(s.get("skipped", 0)) for s in suites)
    duration = sum(float(s.get("time", 0)) for s in suites)

    passed = total - failures - errors - skipped
    pass_rate = passed / total * 100 if total else 0

    return {
        "total": total,
        "passed": passed,
        "failed": failures + errors,
        "skipped": skipped,
        "duration": duration,
        "pass_rate": pass_rate,
    }


if __name__ == "__main__":
    metrics = calculate_metrics("reports/junit.xml")

    print("\nQUALITYFORGE AI - TEST METRICS\n")
    print(f"Total Tests : {metrics['total']}")
    print(f"Passed      : {metrics['passed']}")
    print(f"Failed      : {metrics['failed']}")
    print(f"Skipped     : {metrics['skipped']}")
    print(f"Duration    : {metrics['duration']:.2f} seconds")
    print(f"Pass Rate   : {metrics['pass_rate']:.2f}%")
