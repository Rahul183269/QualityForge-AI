import json

from src.observability import (
    LOG_FILE,
    summarize_with_observability,
)


def test_observability_records_execution_details():
    result = summarize_with_observability(
        error_message="AssertionError: Expected 200 but got 500",
        test_name="test_observability_sample",
    )

    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    event = json.loads(lines[-1])

    assert event["execution_id"]
    assert event["event"] == "failure_analysis"
    assert event["duration_ms"] >= 0
    assert event["result"] == "success"
    assert event["test_name"] == "test_observability_sample"
    assert event["failure_category"] == result["failure_category"]


def test_observability_redacts_sensitive_data():
    summarize_with_observability(
        error_message="AssertionError: API_KEY=demo_secret123",
        test_name="test_redaction_sample",
    )

    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    event = json.loads(lines[-1])

    assert "demo_secret123" not in json.dumps(event)
    assert "[REDACTED]" in json.dumps(event)