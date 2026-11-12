import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(1)

@pytest.mark.smoke
def test_home_page(page):
    expect(page).to_have_title("Playwright Practice Shop")
    expect(page.get_by_role("heading", name="Playwright Practice Shop")).to_be_visible()

def test_browser_context_isolation(browser):
    first, second = browser.new_context(), browser.new_context()
    try:
        first_page, second_page = first.new_page(), second.new_page()
        first_page.goto("data:text/html,<title>Context one</title>")
        second_page.goto("data:text/html,<title>Context two</title>")
        expect(first_page).to_have_title("Context one")
        expect(second_page).to_have_title("Context two")
    finally:
        first.close(); second.close()
