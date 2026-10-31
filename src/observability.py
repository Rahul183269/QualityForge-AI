
import json
import logging
import time
import uuid

from pathlib import Path

from src.ai_failure_summarizer import (
    summarize_failure,
    redact_sensitive_data,
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

LOG_FILE = REPORTS_DIR / "observability.jsonl"

logger = logging.getLogger("qualityforge.observability")
logger.setLevel(logging.INFO)
logger.propagate = False

if not logger.handlers:
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    logger.addHandler(handler)


def log_event(event_data):
    """Write one structured JSON event."""

    logger.info(json.dumps(event_data))


def summarize_with_observability(
    error_message,
    test_name="Unknown test",
    expected_result=None,
    actual_result=None,
):
    execution_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    try:
        result = summarize_failure(
            error_message=error_message,
            test_name=test_name,
            expected_result=expected_result,
            actual_result=actual_result,
        )

        duration_ms = (time.perf_counter() - start_time) * 1000

        event = {
            "execution_id": execution_id,
            "event": "failure_analysis",
            "duration_ms": round(duration_ms, 4),
            "result": "success",
            "test_name": test_name,
            "failure_category": result["failure_category"],
            "error": result["evidence"][0],
        }

        log_event(event)

        return result

    except Exception as error:
        duration_ms = (time.perf_counter() - start_time) * 1000

        event = {
            "execution_id": execution_id,
            "event": "failure_analysis",
            "duration_ms": round(duration_ms, 4),
            "result": "failed",
            "test_name": test_name,
            "error": redact_sensitive_data(str(error)),
        }

        log_event(event)
        raise


if __name__ == "__main__":
    result = summarize_with_observability(
        error_message="AssertionError: Expected 200 but got 500",
        test_name="test_create_user",
        expected_result=200,
        actual_result=500,
    )

    print("\nQUALITYFORGE AI - OBSERVABILITY")
    print("Failure category:", result["failure_category"])
    print("Structured log:", LOG_FILE)
