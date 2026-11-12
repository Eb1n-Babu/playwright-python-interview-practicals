import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(6)

def test_iframe_and_new_tab(page):
    frame = page.frame_locator("iframe[title='Practice frame']")
    frame.get_by_label("Inside frame").fill("Hello frame")
    expect(frame.get_by_label("Inside frame")).to_have_value("Hello frame")
    with page.context.expect_page() as opened:
        page.get_by_role("link", name="Open tab").click()
    tab = opened.value
    try:
        expect(tab.get_by_role("heading", name="Popup ready")).to_be_visible()
    finally:
        tab.close()

def test_javascript_dialog_accept(page):
    seen = []
    page.on("dialog", lambda dialog: (seen.append(dialog.message), dialog.accept()))
    page.evaluate("() => window.alert('hello')")
    assert seen == ["hello"]

def test_popup_event(page):
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open popup").click()
    popup = popup_info.value
    try:
        expect(popup.get_by_role("heading", name="Popup ready")).to_be_visible()
    finally:
        popup.close()
