# Guide notes and interview revision

## Sync and Async APIs

This project uses `playwright.sync_api` with ordinary pytest test functions. Playwright also provides `playwright.async_api` with `async def` and `await`; do not mix the APIs in a test.

## Actionability and useful methods

Before actions, Playwright checks attachment, visibility, stability, enabled state, and whether the target can receive pointer events. Investigate hidden overlays, disabled controls, motion, stale state, or a wrong locator before increasing timeouts. The guide's useful methods include `click()`, `fill()`, `press()`, `check()` / `uncheck()`, `select_option()`, `hover()`, `count()`, `is_visible()`, `text_content()`, `inner_text()`, `get_attribute()` and `evaluate()`.

## Debugging common failures

| Symptom | Likely cause | First response |
|---|---|---|
| TimeoutError | State never became actionable or expected state did not occur | Check selector, URL, overlay, frame and network |
| Strict mode violation | Multiple elements matched | Scope to a parent, filter, or select a stable occurrence |
| Element not found | Wrong selector, page or frame | Inspect DOM and URL; use `frame_locator()` for frames |
| `select_option()` fails | Widget is custom rather than a native `<select>` | Click and choose the visible option |
| Download not captured | Listener registered after the click | Enter `expect_download()` before clicking |
| Flaky test | Fixed sleeps, shared data or race | Use web-first assertions and isolate state |

For local debugging use `pytest --headed`; `page.pause()` is useful during an interactive session. Inspect screenshots and traces before changing waits.

## Git / GitHub interview reminders

Git is distributed version control; GitHub hosts repositories and collaboration. `git add` stages selected changes; `git commit` records the staged snapshot. `git pull` integrates remote changes; `git push` uploads commits. A branch is an independent line of development. `.gitignore` prevents tracking generated files and secrets.

```bash
git status
git switch -c feature/table-practicals
git add tests/test_07_tables.py
git commit -m "Add dynamic table practicals"
git switch main
git merge feature/table-practicals
```

Configure your own identity before committing on a new machine. Add a remote only when you have a repository URL and are ready to publish; this project has no remote configured.

## 30-day roadmap from the guide

| Days | Study target | Deliverable |
|---|---|---|
| 1–3 | Python, pytest, Browser/Context/Page | Explain fixtures and run fundamentals |
| 4–7 | Locators and forms | Write locator and form tests |
| 8–10 | Mouse, keyboard, waits, assertions | Automate dynamic elements without fixed sleeps |
| 11–13 | Dialogs, frames, tabs, tables | Complete table and iframe scenarios |
| 14–16 | Upload/download, screenshots, debugging | Capture evidence and diagnose a failure |
| 17–19 | Fixtures and POM | Create LoginPage and ProductsPage |
| 20–22 | JSON, CSV and API | Parameterize tests and validate API responses |
| 23–25 | Network mocking and authentication | Test success/error and reuse safe state |
| 26–28 | End-to-end and Git | Login, search, cart and commit practice |
| 29–30 | Mock interview and revision | Explain choices and solve a new scenario |

## Interview readiness checklist

- Explain Browser, BrowserContext and Page; use major locators and justify locator choice.
- Automate textboxes, radio buttons, checkboxes, dropdowns, hover, shortcuts and drag/drop.
- Explain auto-waiting and write web-first assertions.
- Handle dialogs, iframes, tabs, dynamic tables, upload/download and screenshots.
- Create fixtures and a simple Page Object Model; run data-driven tests with JSON/CSV.
- Send API requests, mock network behavior, and reuse storage state without committing secrets.
- Automate a user journey, debug with logs/screenshots/traces, and explain basic Git operations.
