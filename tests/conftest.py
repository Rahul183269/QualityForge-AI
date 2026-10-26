from playwright.sync_api import sync_playwright
import pytest
import requests


@pytest.fixture
def api_session():
    session = requests.Session()

    session.headers.update({
        "Accept": "application/json"
    })

    yield session
    return session

@pytest.fixture
def browser_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        yield page

        browser.close()