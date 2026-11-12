import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(15)

@pytest.mark.smoke
def test_search_and_add_two_products(page):
    search = page.get_by_placeholder("Search products")
    search.fill("Phone"); page.get_by_role("button", name="Search").click()
    expect(page.get_by_role("heading", name="Phone")).to_be_visible()
    expect(page.locator("[data-testid='product']").filter(has=page.get_by_role("heading", name="Laptop"))).to_be_hidden()
    page.get_by_role("button", name="Add to cart").click()
    search.fill(""); page.get_by_role("button", name="Search").click()
    page.get_by_role("button", name="Add to cart").nth(1).click()
    expect(page.locator("#cart-count")).to_have_text("2")

def test_registration_user_journey(page):
    page.get_by_label("Username").fill("test-user")
    page.get_by_role("button", name="Create account").click()
    expect(page.locator("#registration-status")).to_have_text("Account created")
