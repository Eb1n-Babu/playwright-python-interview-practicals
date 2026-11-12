import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(9)

@pytest.fixture
def saved_profile(page):
    page.get_by_label("Name", exact=True).fill("Ada")
    page.get_by_role("button", name="Save").click()
    return page.locator("#saved")

def test_fixture_sets_up_reusable_state(saved_profile):
    expect(saved_profile).to_have_text("Saved")
