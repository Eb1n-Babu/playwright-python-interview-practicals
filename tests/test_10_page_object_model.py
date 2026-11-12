import pytest
from pages import LoginPage
from playwright.sync_api import expect

pytestmark = pytest.mark.session(10)

def test_login_page_object(page, base_url):
    login = LoginPage(page).open(base_url).login()
    expect(login.welcome_message).to_have_text("Welcome back")
