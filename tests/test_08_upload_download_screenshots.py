import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.session(8)

def test_upload_download_and_screenshot(page, test_file, tmp_path):
    page.locator("#upload").set_input_files(str(test_file))
    expect(page.locator("#upload")).to_have_value("C:\\fakepath\\upload.txt")
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download sample").click()
    download = download_info.value
    saved = tmp_path / download.suggested_filename
    download.save_as(saved)
    assert saved.read_text(encoding="utf-8") == "Playwright sample download\n"
    page.screenshot(path=str(tmp_path / "page.png"), full_page=True)
    assert (tmp_path / "page.png").stat().st_size > 0
