
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_page_username(browser_page):
    browser_page.set_content("""
        <form>
            <label for="username">Username</label>
            <input id="username" name="username">
            <button type="submit" disabled>Submit</button>
        </form>
    """)

    login_page = LoginPage(browser_page)
    login_page.enter_username("testuser")

    expect(login_page.username).to_have_value("testuser")
