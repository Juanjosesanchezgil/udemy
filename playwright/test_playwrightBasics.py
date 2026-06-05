from playwright.async_api import Page


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


# chromium headless mode, 1 single context
def test_playwrightShortCut(page):
    page.goto("https://rahulshettyacademy.com")
