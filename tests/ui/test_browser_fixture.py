
from playwright.sync_api import expect


def test_browser_page_fixture(browser_page):
    browser_page.set_content("""
        <h1>QualityForge AI</h1>
    """)

    heading = browser_page.get_by_role(
        "heading",
        name="QualityForge AI",
    )

    expect(heading).to_be_visible()
