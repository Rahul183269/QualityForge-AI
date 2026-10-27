
import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_homepage_heading_across_browsers(browser_name):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)
        browser = browser_type.launch()
        page = browser.new_page()

        page.set_content("""
            <html>
                <head><title>QualityForge AI</title></head>
                <body>
                    <h1>QualityForge AI</h1>
                </body>
            </html>
        """)

        heading = page.get_by_role(
            "heading",
            name="QualityForge AI",
        )

        expect(heading).to_be_visible()

        browser.close()
