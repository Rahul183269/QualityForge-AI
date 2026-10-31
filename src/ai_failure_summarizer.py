
from scripts.failure_analyzer import classify_failure


def summarize_failure(
    error_message,
    test_name="Unknown test",
    expected_result=None,
    actual_result=None,
):
    if not isinstance(error_message, str) or not error_message.strip():
        raise ValueError("A valid error message is required")

    category = classify_failure(error_message)

    evidence = [error_message.strip()]

    if expected_result is not None:
        evidence.append(f"Expected: {expected_result}")

    if actual_result is not None:
        evidence.append(f"Actual: {actual_result}")

    possible_causes = {
        "assertion": [
            "Application behavior differs from expected behavior",
            "Incorrect test data or assertion",
        ],
        "environment": [
            "Browser or execution environment is unavailable",
            "Environment configuration may be incorrect",
        ],
        "network": [
            "Service may be unavailable",
            "Network connectivity or timeout issue",
        ],
        "setup": [
            "Required dependency or configuration may be missing",
        ],
        "unknown": [
            "Insufficient information to identify the root cause",
        ],
    }

    recommended_steps = {
        "assertion": [
            "Compare expected and actual results",
            "Inspect the application response",
            "Verify the test assertion and test data",
        ],
        "environment": [
            "Verify browser installation",
            "Check environment configuration",
            "Review execution logs",
        ],
        "network": [
            "Check service availability",
            "Verify endpoint and port",
            "Inspect network and timeout logs",
        ],
        "setup": [
            "Check required dependencies",
            "Verify configuration and file paths",
        ],
        "unknown": [
            "Inspect the complete error message",
            "Collect additional logs",
            "Investigate the failure manually",
        ],
    }

    summary = (
        f"Test '{test_name}' encountered an "
        f"{category.title()} failure."
    )

    return {
        "test_name": test_name,
        "failure_category": category,
        "summary": summary,
        "evidence": evidence,
        "possible_causes": possible_causes[category],
        "recommended_steps": recommended_steps[category],
        "confidence": "Low",
        "limitations": (
            "This is a rule-based analysis. "
            "The root cause is not confirmed."
        ),
    }


if __name__ == "__main__":
    result = summarize_failure(
        error_message="AssertionError: Expected 200 but got 500",
        test_name="test_create_user",
        expected_result=200,
        actual_result=500,
    )

    print("\nQUALITYFORGE AI - FAILURE SUMMARY\n")

    for key, value in result.items():
        print(f"{key}: {value}")
