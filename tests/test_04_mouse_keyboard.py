import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(4)

def test_hover_double_right_click_and_keyboard(page):
    page.locator("#menu").hover()
    expect(page.get_by_role("link", name="Submenu item")).to_be_visible()
    page.get_by_role("button", name="Open", exact=True).dblclick()
    search = page.get_by_role("textbox", name="Search", exact=True)
    search.fill("old text"); search.press("Control+A"); search.press("Backspace")
    expect(search).to_be_empty()
    page.get_by_role("button", name="Options").click(button="right")

def test_drag_and_drop(page):
    page.locator("#source").drag_to(page.locator("#drop-target"))
    expect(page.locator("#drop-target")).to_have_text("Drag me")
