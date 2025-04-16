from .base_page import BasePage

class WebFormPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://www.selenium.dev/selenium/web/web-form.html"

    def load(self):
        self.visit(self.url)

    def fill_form(self, username, password):
        self.fill_input("input[name='my-text']", username)
        self.fill_input("input[name='my-password']", password)
        self.select_option("select[name='my-select']", "2")
        self.check("input[name='my-check']")

    def submit(self):
        self.click("button")

    def get_submission_heading(self):
        return self.get_text("h1")

    def get_submission_message(self):
        return self.get_text("#message")
