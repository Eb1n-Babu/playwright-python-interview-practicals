import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(3)

def test_text_inputs_radio_checkbox_and_dropdowns(page):
    email = page.get_by_label("Email")
    email.fill("qa@example.com"); expect(email).to_have_value("qa@example.com")
    email.fill(""); expect(email).to_be_empty()
    page.get_by_label("Other").check(); expect(page.get_by_label("Other")).to_be_checked()
    terms = page.get_by_label("Accept terms")
    terms.check(); expect(terms).to_be_checked(); terms.uncheck(); expect(terms).not_to_be_checked()
    page.get_by_label("City").select_option("kochi")
    expect(page.get_by_label("City")).to_have_value("kochi")
    page.get_by_label("Skills").select_option(["py", "pw"])
    expect(page.get_by_label("Skills")).to_have_values(["py", "pw"])

def test_form_submit_and_validation(page):
    page.get_by_role("button", name="Create account").click()
    expect(page.locator("#register input[required]")).to_be_visible()
    page.get_by_label("Username").fill("learner")
    page.get_by_role("button", name="Create account").click()
    expect(page.locator("#registration-status")).to_have_text("Account created")
