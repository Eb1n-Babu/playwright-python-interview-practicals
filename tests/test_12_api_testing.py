import pytest

pytestmark = pytest.mark.session(12)

def test_api_request_against_local_demo(playwright, base_url):
    request = playwright.request.new_context()
    try:
        response = request.get(base_url + "/sample.txt")
        assert response.status == 200
        assert "Playwright sample" in response.text()
        assert "text/plain" in response.headers.get("content-type", "")
    finally:
        request.dispose()
