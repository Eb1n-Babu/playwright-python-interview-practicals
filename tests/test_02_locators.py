import re
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(2)

def test_user_facing_locators(page):
    expect(page.get_by_role("button", name="Save")).to_be_visible()
    expect(page.get_by_text("Profile", exact=True)).to_be_visible()
    page.get_by_label("Email").fill("qa@example.com")
    expect(page.get_by_placeholder("Enter email")).to_have_value("qa@example.com")
    expect(page.get_by_alt_text("Company logo")).to_be_visible()
    expect(page.get_by_title("Brand mark")).to_be_visible()
    expect(page.get_by_test_id("save-button")).to_be_visible()

def test_css_selector_coverage(page):
    selectors = ["input", "#email", ".card", "[type='email']", "input[name='email']",
                 "section > h2", "header a", "input:not([type='radio'])", "tr:nth-child(2)",
                 "button:has-text('Save')"]
    for selector in selectors:
        assert page.locator(selector).count() > 0, f"CSS selector did not match: {selector}"

def test_xpath_selector_coverage(page):
    selectors = ["//input", "//*[@id='email']", "//*[contains(@class,'card')]",
                 "//input[@name='email' and @type='email']", "//button[normalize-space()='Save']",
                 "//button[contains(normalize-space(.),'Sav')]", "(//button)[1]",
                 "//section//label[input[@id='email']]", "//h1/following::a[1]",
                 "//tr[td[normalize-space()='Ada']]//button", "//input[@type='checkbox']"]
    for selector in selectors:
        assert page.locator("xpath=" + selector).count() > 0, f"XPath did not match: {selector}"

def test_filter_chaining_and_nth(page):
    rows = page.locator("tbody tr")
    expect(rows).to_have_count(2)
    active = rows.filter(has=page.locator("td:nth-child(2)").filter(has_text=re.compile("^Active$")))
    expect(active.get_by_role("button", name="Edit")).to_be_visible()
    expect(rows.nth(1).locator("td").nth(0)).to_have_text("Lin")
    cards = page.get_by_test_id("product")
    expect(cards.filter(has=page.get_by_role("heading", name="Phone"))).to_have_count(1)
