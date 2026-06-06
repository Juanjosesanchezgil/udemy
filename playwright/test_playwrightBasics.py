from playwright.async_api import Page


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


# chromium headless mode, 1 single context
def test_playwrightShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")  # type: ignore


def test_coreLocators(page: Page):
    page.goto(
        "https://rahulshettyacademy.com/loginpagePractise/")  # type: ignore
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")