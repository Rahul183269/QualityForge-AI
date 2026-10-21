from playwright.sync_api import sync_playwright


def test_learn_more_link():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        try:
            page.goto("https://example.com", wait_until="load")

            link = page.get_by_role("link", name="Learn more")

            assert link.is_visible()
            assert link.get_attribute("href") == (
                "https://iana.org/help/example-domains"
            )

        finally:
            browser.close()