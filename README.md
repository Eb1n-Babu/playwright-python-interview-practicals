# Playwright with Python: Complete Practical Study Project

Runnable companion project for **Playwright with Python — Complete Practical Interview Study Guide**. It follows the PDF's 16 numbered sessions and uses its Sync API, pytest, Browser / BrowserContext / Page terminology, and learning progression. The tests use a small local practice site and local API responses, so the standard suite does not depend on a third-party website or Internet access.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

macOS/Linux: create with `python3 -m venv .venv`, activate with `source .venv/bin/activate`, then use the same pip and Playwright install commands. The project expects Python 3.9+.

## Run

```powershell
pytest
pytest tests/test_02_locators.py
pytest -k get_by_role
pytest -m smoke
pytest --headed
pytest -n 2
pytest --html=playwright-report/report.html --self-contained-html
```

`conftest.py` starts and shuts down an ephemeral localhost demo server automatically. Browser tracing and failure screenshots are configured in `pytest.ini`; artifacts go under `test-results/` and are ignored by Git. Install Chromium once with `playwright install chromium` before running tests.

## Session map

| Session | Guide topic | Practical |
|---|---|---|
| 1 | Python, pytest and Playwright fundamentals | Browser, isolated BrowserContexts, Page, assertions |
| 2 | All important Playwright locators | Role/text/label/placeholder/alt/title/test ID, filters, chaining, CSS and XPath |
| 3 | Form controls | Text entry, radio, checkbox, native and multiple select, validation |
| 4 | Mouse and keyboard actions | Hover, double/right click, keyboard shortcuts, drag and drop |
| 5 | Waits and assertions | Auto-waiting, locator state, URL and web-first assertions |
| 6 | Alerts, frames and multiple tabs | Dialogs, iframe, new tab and popup |
| 7 | Dynamic tables | Rows, cells, scoped actions |
| 8 | Upload, download and screenshots | File chooser input, captured download and evidence |
| 9 | Fixtures | Reusable setup and teardown |
| 10 | Page Object Model | `pages.LoginPage` |
| 11 | Data-driven testing | pytest parameterize, JSON and CSV |
| 12 | API testing | Playwright APIRequestContext, status, body and headers |
| 13 | Network interception and mocking | Fulfill, error response and POST payload inspection |
| 14 | Authentication, cookies and storage state | localStorage persistence and state reuse; generated state is temporary |
| 15 | Real-world end-to-end scenarios | Registration, search and cart |
| 16 | Test organization, reports, retries and parallel execution | markers, reports, traces and xdist |

Extra guide material is in this README and `docs/guide-notes.md`: Sync vs Async API, actionability checks, useful methods, debugging, common errors, Git/GitHub workflow, interview prompts, and the 30-day roadmap.

## CSS and XPath coverage

Session 2 has runnable examples for tag, ID, class, attribute, descendant/child, pseudo-class, `:not()` and text matching CSS. XPath examples cover tag and wildcard, ID/class/attribute predicates, `and`, exact and partial text, normalized text, positional selection, descendant/child relationships, parent scoping, and the `following` axis. Prefer user-facing locators where possible; use short stable CSS/XPath selectors where the guide's DOM-oriented examples are useful. XPath is deliberately relative; brittle absolute paths are not taught as a preferred pattern.

## Expected result

After installing dependencies and Chromium, `pytest` should report all collected tests passing. It may report a different count as you add practice exercises. A failed test produces pytest's failure detail and configured trace/screenshot artifacts. Use `playwright show-trace <trace.zip>` to inspect a retained trace.

## Error handling and debugging

Read the first meaningful error, verify the URL/title and locator count, and inspect the relevant page or frame before changing timeouts. Scope duplicate matches to a parent, use `frame_locator()` for iframes, register `expect_download()` before clicking, and prefer web-first assertions over fixed sleeps. The local server fixture always shuts down in teardown. Tests create isolated browser contexts and temporary files.

## Git study workflow

The repository is initialized with meaningful commits grouped by setup, each session, documentation, and final verification. For future practice use `git status`, stage only the session you completed, and commit with a message such as `Complete locator practicals`. Branches, merge, pull and push examples are in `docs/guide-notes.md`. No remote is configured.
