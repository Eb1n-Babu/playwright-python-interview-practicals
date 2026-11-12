import csv
import json
from pathlib import Path
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(11)
ROOT = Path(__file__).parents[1]
USERS = json.loads((ROOT / "test_data/users.json").read_text(encoding="utf-8"))

@pytest.mark.parametrize("user", USERS, ids=lambda user: user["username"])
def test_json_parameterized_registration(page, user):
    page.get_by_label("Username").fill(user["username"])
    page.get_by_role("button", name="Create account").click()
    expect(page.locator("#registration-status")).to_have_text(user["expected"])

def test_csv_test_data(page):
    with (ROOT / "test_data/users.csv").open(encoding="utf-8", newline="") as stream:
        users = list(csv.DictReader(stream))
    assert len(users) == 2
    page.get_by_label("Username").fill(users[0]["username"])
    page.get_by_role("button", name="Create account").click()
    expect(page.locator("#registration-status")).to_have_text(users[0]["expected"])
