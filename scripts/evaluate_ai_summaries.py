
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.ai_failure_summarizer import summarize_failure

DATASET_PATH = PROJECT_ROOT / "test_data" / "ai_evaluation_cases.json"
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORT_PATH = REPORTS_DIR / "ai_evaluation_latest.json"

# Version registry
VERSIONS = {
    "model_provider": "rule-based-v1",
    "prompt": "prompt-v1",
    "dataset": "dataset-v1",
    "evaluation": "evaluator-v1",
}


def evaluate_case(case):
    case_id = case["id"]
    message = case["input"]

    if case_id == "TC007":
        try:
            summarize_failure(message)
            return False, "Empty input was not rejected"
        except ValueError:
            return True, "Empty input correctly rejected"

    if case_id == "TC008":
        message = message * case["repeat_count"]

    expected = case["expected_category"]

    result = summarize_failure(
        error_message=message,
        test_name=case["name"],
        expected_result=200 if case_id == "TC001" else None,
        actual_result=500 if case_id == "TC001" else None,
    )

    if result["failure_category"] != expected:
        return False, (
            f"Expected category {expected}, "
            f"got {result['failure_category']}"
        )

    output = json.dumps(result).lower()

    checks = {
        "TC001": ["expected: 200", "actual: 500"],
        "TC002": ["connection refused", "service availability"],
        "TC003": [
            "browser executable not found",
            "browser installation",
        ],
        "TC004": ["modulenotfounderror", "required dependencies"],
        "TC005": ["insufficient information", "not confirmed"],
        "TC006": ["[redacted]"],
        "TC008": ["truncated"],
    }

    for finding in checks.get(case_id, []):
        if finding not in output:
            return False, f"Missing key finding: {finding}"

    if case_id == "TC006" and "demo_secret123" in output:
        return False, "Sensitive information was exposed"

    if case_id == "TC008" and len(result["evidence"][0]) != 10000:
        return False, "Long input was not truncated correctly"

    return True, "All evaluation checks passed"


def run_evaluation():
    run_id = str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).isoformat()

    with DATASET_PATH.open(encoding="utf-8") as file:
        dataset = json.load(file)

    passed = 0
    failed = 0
    case_results = []

    print("\nQUALITYFORGE AI - REGRESSION EVALUATION\n")
    print(f"Run ID: {run_id}")

    for case in dataset["cases"]:
        try:
            success, message = evaluate_case(case)
        except Exception as error:
            success = False
            message = f"Evaluation error: {error}"

        status = "PASS" if success else "FAIL"

        print(f"{case['id']} - {case['name']}: {status}")
        print(f"  {message}")

        case_results.append({
            "case_id": case["id"],
            "name": case["name"],
            "status": status,
            "message": message,
        })

        if success:
            passed += 1
        else:
            failed += 1

    total = passed + failed
    gate = "PASSED" if failed == 0 else "FAILED"

    report = {
        "run_id": run_id,
        "timestamp_utc": timestamp,
        "versions": VERSIONS,
        "dataset_file": str(DATASET_PATH.relative_to(PROJECT_ROOT)),
        "summary": {
            "total_cases": total,
            "passed": passed,
            "failed": failed,
            "pass_rate_percent": round(
                (passed / total) * 100, 2
            ) if total else 0,
            "regression_gate": gate,
        },
        "cases": case_results,
    }

    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8",
    )

    print("\nEVALUATION SUMMARY")
    print(f"Total Cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")
    print(f"Regression Gate: {gate}")
    print(f"\nJSON Report: {REPORT_PATH}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(run_evaluation())
