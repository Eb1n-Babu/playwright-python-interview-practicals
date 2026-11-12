import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(14)

def test_local_storage_and_storage_state(browser, base_url, tmp_path):
    state = tmp_path / "auth.json"
    context = browser.new_context()
    try:
        page = context.new_page(); page.goto(base_url + "/index.html")
        page.get_by_role("button", name="Login").click()
        expect(page.locator("#auth-status")).to_have_text("Welcome back")
        context.storage_state(path=str(state))
    finally:
        context.close()
    restored = browser.new_context(storage_state=str(state))
    try:
        authenticated = restored.new_page(); authenticated.goto(base_url + "/index.html")
        assert authenticated.evaluate("localStorage.getItem('auth')") == "yes"
    finally:
        restored.close()
