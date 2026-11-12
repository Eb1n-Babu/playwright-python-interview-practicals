from pathlib import Path
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import pytest

ROOT = Path(__file__).parent
DEMO = ROOT / "demo"


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


@pytest.fixture(scope="session")
def demo_server():
    handler = lambda *args, **kwargs: QuietHandler(*args, directory=str(DEMO), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


@pytest.fixture
def base_url(demo_server):
    return demo_server


@pytest.fixture
def page(browser, base_url):
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    page.set_default_timeout(8000)
    page.goto(base_url + "/index.html")
    yield page
    context.close()


@pytest.fixture
def test_file(tmp_path):
    path = tmp_path / "upload.txt"
    path.write_text("Playwright fixture upload", encoding="utf-8")
    return path
