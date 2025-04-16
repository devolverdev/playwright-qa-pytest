import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from playwright.sync_api import sync_playwright
from pages.web_form_page import WebFormPage
from config.secrets import USERNAME, PASSWORD


@pytest.mark.form
def test_form_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        form = WebFormPage(page)
        form.load()
        form.fill_form(USERNAME, PASSWORD)
        form.submit()

        heading = form.get_submission_heading()
        message = form.get_submission_message()

        assert heading.strip() == "Form submitted"
        assert message.strip() == "Received!"

        browser.close()
