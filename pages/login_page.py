
from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username = page.get_by_label("Username")
        self.submit_button = page.get_by_role(
            "button",
            name="Submit",
        )

    def enter_username(self, username: str):
        self.username.fill(username)

    def click_submit(self):
        self.submit_button.click()
