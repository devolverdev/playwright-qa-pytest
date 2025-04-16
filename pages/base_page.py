from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url)

    def fill_input(self, selector: str, text: str):
        self.page.fill(selector, text)

    def click(self, selector: str):
        self.page.click(selector)

    def select_option(self, selector: str, value: str):
        self.page.select_option(selector, value)

    def check(self, selector: str):
        self.page.check(selector)

    def get_text(self, selector: str):
        return self.page.inner_text(selector)

    def take_screenshot(self, path: str = "screenshot.png"):
        self.page.screenshot(path=path)
