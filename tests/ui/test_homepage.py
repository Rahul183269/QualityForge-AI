from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, expect


def test_learn_more_link():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        try:
            page.goto("https://example.com", wait_until="load")

            link = page.get_by_role("link", name="Learn more")
            expect(link).to_have_count(1)

            expect(link).to_be_visible()
            expect(link).to_have_attribute(
                "href",
                "https://iana.org/help/example-domains",
            )

            link.click()
            page.wait_for_url("https://www.iana.org/help/example-domains")
            
        finally:
            browser.close()

def test_homepage_message():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        try:
            page.goto("https://example.com", wait_until="load")

            message = page.get_by_text(
                "This domain is for use in documentation examples",
                exact=False,
            )

            expect(message).to_be_visible()

        finally:
            browser.close()


def test_form_interaction():
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
                <p id="result" hidden></p>

                <script>
                    document.querySelector("form").addEventListener(
                        "submit", function(event) {
                            event.preventDefault();
                            document.querySelector("#result").textContent =
                                "Form submitted successfully";
                        }
                    );
                </script>
            """)

            username = page.get_by_label("Username")
            result_message = page.locator("#result")
            expect(result_message).to_be_hidden()
            expect(username).to_be_visible()
            submit_button = page.get_by_role("button", name="Submit")
            expect(submit_button).to_be_disabled()
            expect(submit_button).to_be_visible()
            username.fill("testuser")

            expect(username).to_have_value("testuser")

            

            expect(username).to_be_enabled()

        finally:
            browser.close()