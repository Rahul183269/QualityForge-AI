
from playwright.sync_api import sync_playwright, expect

from pages.login_page import LoginPage


def test_login_page_username():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        try:
            page.set_content("""
                <form>
                    <label for="username">Username</label>
                    <input id="username" name="username">
                    <button type="submit" disabled>Submit</button>
                </form>
            """)

            login_page = LoginPage(page)
            login_page.enter_username("testuser")

            expect(
                page.get_by_label("Username")
            ).to_have_value("testuser")

        finally:
            browser.close()
