import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(16)

@pytest.mark.smoke
def test_critical_shop_heading(page):
    expect(page.get_by_role("heading", name="Playwright Practice Shop")).to_be_visible()

@pytest.mark.regression
def test_regression_profile_save(page):
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_role("status")).to_have_text("Saved")
