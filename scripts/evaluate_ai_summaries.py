
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.ai_failure_summarizer import summarize_failure

DATASET_PATH = PROJECT_ROOT / "test_data" / "ai_evaluation_cases.json"

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

    # Check failure classification
    if result["failure_category"] != expected:
        return False, (
            f"Expected category {expected}, "
            f"got {result['failure_category']}"
        )

    output = json.dumps(result).lower()

    # Case-specific key finding checks
    checks = {
        "TC001": [
            "expected: 200",
            "actual: 500",
        ],
        "TC002": [
            "connection refused",
            "service availability",
        ],
        "TC003": [
            "browser executable not found",
            "browser installation",
        ],
        "TC004": [
            "modulenotfounderror",
            "required dependencies",
        ],
        "TC005": [
            "insufficient information",
            "not confirmed",
        ],
        "TC006": [
            "[redacted]",
        ],
        "TC008": [
            "truncated",
        ],
    }

    for finding in checks.get(case_id, []):
        if finding not in output:
            return False, f"Missing key finding: {finding}"

    # Verify that sensitive information is not exposed
    if case_id == "TC006":
        if "demo_secret123" in output:
            return False, "Sensitive information was exposed"

    # Verify long input is limited
    if case_id == "TC008":
        if len(result["evidence"][0]) != 10000:
            return False, "Long input was not truncated correctly"

    return True, "All evaluation checks passed"


def run_evaluation():
    with DATASET_PATH.open(encoding="utf-8") as file:
        dataset = json.load(file)

    passed = 0
    failed = 0

    print("\nQUALITYFORGE AI - REGRESSION EVALUATION\n")

    for case in dataset["cases"]:
        try:
            success, message = evaluate_case(case)
        except Exception as error:
            success = False
            message = f"Evaluation error: {error}"

        status = "PASS" if success else "FAIL"

        print(f"{case['id']} - {case['name']}: {status}")
        print(f"  {message}")

        if success:
            passed += 1
        else:
            failed += 1

    total = passed + failed

    print("\nEVALUATION SUMMARY")
    print(f"Total Cases : {total}")
    print(f"Passed      : {passed}")
    print(f"Failed      : {failed}")

    if failed:
        print("\nREGRESSION GATE: FAILED")
        return 1

    print("\nREGRESSION GATE: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_evaluation())
