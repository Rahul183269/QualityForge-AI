
import statistics
import time
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.ai_failure_summarizer import summarize_failure


SAMPLE_FAILURES = [
    "AssertionError: Expected 200 but got 500",
    "ConnectionError: Connection refused",
    "ModuleNotFoundError: No module named requests",
    "Unexpected application response",
]

RUNS_PER_CASE = 10


def measure_latency(error_message):
    durations = []

    for _ in range(RUNS_PER_CASE):
        start = time.perf_counter()

        summarize_failure(
            error_message=error_message,
            test_name="benchmark_test",
        )

        elapsed = time.perf_counter() - start
        durations.append(elapsed * 1000)

    return {
        "average_ms": statistics.mean(durations),
        "minimum_ms": min(durations),
        "maximum_ms": max(durations),
    }


def main():
    print("\nQUALITYFORGE AI - EFFICIENCY METRICS\n")

    for index, failure in enumerate(SAMPLE_FAILURES, start=1):
        metrics = measure_latency(failure)

        print(f"Sample {index}")
        print(f"Average latency: {metrics['average_ms']:.4f} ms")
        print(f"Minimum latency: {metrics['minimum_ms']:.4f} ms")
        print(f"Maximum latency: {metrics['maximum_ms']:.4f} ms")
        print("-" * 40)

    print("\nTOKEN USAGE: Unavailable")
    print("API COST: Unavailable")
    print("Reason: No external AI provider is connected.")


if __name__ == "__main__":
    main()
