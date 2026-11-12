import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(7)

def test_find_dynamic_table_row_and_cells(page):
    ada = page.locator("tbody tr").filter(has_text="Ada")
    expect(ada.locator("td").nth(1)).to_have_text("Active")
    ada.get_by_role("button", name="Edit").click()
    expect(ada).to_have_count(1)
    assert page.locator("tbody tr").count() == 2
