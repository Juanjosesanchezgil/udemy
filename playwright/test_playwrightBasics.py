from playwright.async_api import Page
import time


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
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("button", name="Sign in").click()

    time.sleep(5)
