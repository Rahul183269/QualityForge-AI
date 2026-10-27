
# QualityForge AI - Test Coverage Summary

## Test Execution Results

| Test Layer | Result |
|---|---:|
| API tests | 14 passed |
| UI tests | 7 passed |
| Full test suite | 41 passed |

## Test Categories

### API Testing
- Validates API endpoints and HTTP responses.
- Runs independently using pytest.

### UI Testing
- Validates browser behavior and visible elements.
- Includes Chromium and Firefox smoke tests.
- Uses Playwright and pytest.

### Project Validation
- Includes project setup and validation tests.

## Current Limitations
- API and UI tests currently run as separate suites.
- Cross-browser coverage currently includes Chromium and Firefox.
- End-to-end integration between a real UI and backend has not yet been established.

## Verification Command

Run the complete suite with:

    .\.venv\Scripts\python.exe -m pytest -v
