import json
import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(13)

def test_route_fulfill_mock_response(page):
    page.route("**/api/products", lambda route: route.fulfill(status=200, content_type="application/json", body='[{"id":1,"name":"Mock Laptop"}]'))
    response = page.evaluate("async () => (await fetch('/api/products')).json()")
    assert response == [{"id": 1, "name": "Mock Laptop"}]

def test_route_abort_and_server_error(page):
    page.route("**/api/fail", lambda route: route.fulfill(status=500, body="server error"))
    response = page.evaluate("async () => { const r=await fetch('/api/fail'); return r.status }")
    assert response == 500

def test_inspect_post_payload(page):
    received = []
    page.route("**/api/submit", lambda route: (received.append(route.request.post_data_json), route.fulfill(status=201, body="created")))
    page.evaluate("async () => fetch('/api/submit',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({name:'Ada'})})")
    assert received == [{"name": "Ada"}]
