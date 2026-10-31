
import re


FAILURE_PATTERNS = {
    "assertion": [
        r"assertionerror",
        r"assert .* failed",
        r"expected .* (but )?got",
    ],
    "environment": [
        r"browser.*not found",
        r"executable doesn't exist",
        r"environment.*not available",
    ],
    "network": [
        r"connectionerror",
        r"connection refused",
        r"timeout",
        r"timed out",
    ],
    "setup": [
        r"modulenotfounderror",
        r"filenotfounderror",
        r"missing.*configuration",
        r"missing.*environment variable",
    ],
}


def classify_failure(error_message):
    message = error_message.lower()

    for category, patterns in FAILURE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, message):
                return category

    return "unknown"


def analyze_failures(failures):
    summary = {
        category: 0
        for category in FAILURE_PATTERNS
    }
    summary["unknown"] = 0

    for failure in failures:
        category = classify_failure(failure)
        summary[category] += 1

    return summary


if __name__ == "__main__":
    sample_failures = [
        "AssertionError: Expected 200 but got 500",
        "Browser executable doesn't exist",
        "ConnectionError: Connection refused",
        "ModuleNotFoundError: No module named requests",
        "Unexpected application response",
        "AssertionError: assert 10 == 20",
        "TimeoutError: API request timed out",
        "FileNotFoundError: config.json",
        "ConnectionError: Max retries exceeded",
        "Some unexpected database error",
        ]

    results = analyze_failures(sample_failures)

    print("\nQUALITYFORGE AI - FAILURE ANALYSIS\n")

    for category, count in results.items():
        print(f"{category.title():12}: {count}")
