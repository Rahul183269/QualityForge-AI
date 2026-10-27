
# API vs UI Testing

## API Testing
- Tests backend endpoints and HTTP responses.
- Uses Python requests and pytest.
- Validates status codes, response data, and error handling.

## UI Testing
- Tests the application through the browser.
- Uses Playwright and pytest.
- Validates elements, user interactions, and visible results.

## Combined Testing Strategy
- Use API tests for fast backend validation.
- Use UI tests for important user journeys.
- Use both to investigate whether a failure is in the backend or user interface.
- Verify API and UI integration when a test application is available.


## Example: API Succeeds but UI Fails

Scenario:
- The registration API returns HTTP 201 Created.
- The UI displays an error message.

Investigation:
1. Verify the API status code and response body.
2. Check whether the UI receives the expected response.
3. Inspect the UI logic that processes the response.
4. Check browser console errors and network requests.
5. Record the root cause and add a regression test.

Expected outcome:
Identify whether the defect is in the backend, the UI, or the integration between them.
