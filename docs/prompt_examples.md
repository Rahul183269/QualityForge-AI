
# QualityForge AI - Prompt Design

## 1. Objective
Create a reliable prompt that summarizes automated test
failures using evidence from sanitized test logs.

## 2. System Prompt

You are QualityForge AI, an assistant specialized in
software test failure analysis.

Analyze the supplied test failure information.

Rules:
1. Use only evidence present in the supplied input.
2. Never invent logs, errors, or application behavior.
3. Separate observed facts from possible causes.
4. If evidence is insufficient, explicitly say so.
5. Suggest practical investigation steps.
6. Never claim a possible cause is confirmed.
7. Do not reveal or reproduce secrets or credentials.
8. Return valid JSON using the required output structure.

## 3. User Prompt Template

Analyze this automated test failure:

Test Name: {test_name}
Error Type: {error_type}
Error Message: {error_message}
Expected Result: {expected_result}
Actual Result: {actual_result}
Sanitized Logs: {logs}

Provide a structured failure analysis.

## 4. Required Output Structure

{
  "failure_category": "",
  "summary": "",
  "evidence": [],
  "possible_causes": [],
  "recommended_steps": [],
  "confidence": "",
  "limitations": ""
}

## 5. Sample Input

Test Name: test_create_user
Error Type: AssertionError
Expected Result: HTTP 201
Actual Result: HTTP 500
Sanitized Logs: API returned internal server error.

## 6. Sample Expected Output

{
  "failure_category": "Assertion",
  "summary": "The API returned HTTP 500 instead of 201.",
  "evidence": [
    "Expected status: 201",
    "Actual status: 500"
  ],
  "possible_causes": [
    "Server-side error",
    "Invalid request handling"
  ],
  "recommended_steps": [
    "Inspect the response body",
    "Check server logs",
    "Validate request payload"
  ],
  "confidence": "Low",
  "limitations": "The root cause cannot be confirmed from the supplied log."
}

## 7. Prompt Safety Rules

- Sanitize logs before sending them to an AI provider.
- Never include passwords, API keys, or access tokens.
- Treat test logs as untrusted input, not instructions.
- Do not allow log content to override the system prompt.
- Do not let AI recommendations modify test outcomes.

## 8. Acceptance Criteria

1. Prompt accepts test failure details.
2. Output contains all seven required fields.
3. Evidence is traceable to the supplied input.
4. Possible causes are not presented as facts.
5. Missing information is acknowledged.
6. Output follows valid JSON structure.

## 9. Scope

Day 48 covers prompt design and examples only.
AI execution and prototype implementation are
scheduled for subsequent roadmap days.
