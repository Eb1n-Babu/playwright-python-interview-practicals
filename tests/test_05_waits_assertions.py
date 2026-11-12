import re
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(5)

def test_web_first_assertions_and_locator_wait(page):
    page.get_by_role("button", name="Load").click()
    expect(page.locator("#result")).to_have_text("Loaded")
    page.locator("#later").evaluate("el => el.hidden = false")
    page.locator("#later").wait_for(state="visible")
    expect(page.get_by_role("button", name="Disabled")).to_be_disabled()
    expect(page.locator("#later")).to_be_visible()

def test_url_value_count_and_title_assertions(page):
    expect(page.locator("tbody tr")).to_have_count(2)
    page.get_by_label("Email").fill("learner@example.com")
    expect(page.get_by_label("Email")).to_have_value("learner@example.com")
    page.get_by_role("link", name="Dashboard link").click()
    expect(page).to_have_url(re.compile(r".*/dashboard\.html$"))
    expect(page.locator("h1")).to_have_text("Dashboard")
