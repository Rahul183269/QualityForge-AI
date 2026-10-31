
import pytest

from src.ai_failure_summarizer import summarize_failure


def test_required_output_fields():
    result = summarize_failure(
        "AssertionError: Expected 200 but got 500"
    )

    required_fields = {
        "test_name",
        "failure_category",
        "summary",
        "evidence",
        "possible_causes",
        "recommended_steps",
        "confidence",
        "limitations",
    }

    assert required_fields.issubset(result.keys())


def test_empty_input_is_rejected():
    with pytest.raises(ValueError):
        summarize_failure("")


def test_long_input_is_truncated():
    long_message = "Unexpected error " * 1000

    result = summarize_failure(long_message)

    assert len(result["evidence"][0]) == 10000
    assert "truncated" in result["limitations"]


def test_sensitive_data_is_redacted():
    message = (
        "AssertionError: API_KEY=secret123 "
        "password=mypassword"
    )

    result = summarize_failure(message)

    evidence = result["evidence"][0]

    assert "secret123" not in evidence
    assert "mypassword" not in evidence
    assert "[REDACTED]" in evidence


def test_unsupported_root_cause_is_not_confirmed():
    result = summarize_failure(
        "Unexpected application response"
    )

    assert result["failure_category"] == "unknown"
    assert "not confirmed" in result["limitations"]
    assert result["confidence"] == "Low"
