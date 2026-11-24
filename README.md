# Autotests for Buggy Cars Rating

[![Tests](https://github.com/MahriMK/buggy-cars-autotests/actions/workflows/tests.yml/badge.svg)](https://github.com/MahriMK/buggy-cars-autotests/actions/workflows/tests.yml)

A test automation practice project for the [Buggy Cars Rating](https://buggy.justtestit.org/) website.
The tests are written in Python with Playwright and pytest, using the Page Object and Page Element patterns.
Tests run automatically in GitHub Actions after every `git push`.

## Tech stack

- Python 3.13
- Playwright (pytest-playwright)
- pytest, pytest-html
- GitHub Actions

## Project structure

```text
├── .github/workflows/tests.yml   # runs the tests in GitHub Actions
├── components/                   # Page Elements: repeating page blocks
│   ├── header.py                 #   site header (login, Register, Profile, Logout)
│   └── pagination.py             #   pagination panel
├── pages/                        # Page Objects: site pages
│   ├── home_page.py
│   ├── overall_rating_page.py
│   └── register_page.py
├── tests/
│   ├── test_home.py              # home page
│   ├── test_register.py          # registration and field validation
│   ├── test_login.py             # login, profile, logout
│   ├── test_pagination.py        # pagination
│   └── test_browser_state.py     # cookies, storage, saved login state
├── conftest.py                   # fixtures
├── pytest.ini                    # pytest settings
└── requirements.txt
```

## How to run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest
```

Useful options:

```bash
pytest --headed                  # with a visible browser window
pytest -m smoke                  # smoke tests only
pytest tests/test_register.py    # a single file
pytest --html=report.html --self-contained-html   # HTML report
```

## What is covered

- Home page: headings, blocks, header elements.
- Registration: navigation, cancel, existing login, mismatched passwords, invalid passwords (one broken rule per password), empty required fields.
- Login and logout: profile and logout links, opening the profile, logging out.
- Pagination: moving to the next page, behavior on the last page.
- Browser: cookies, localStorage and sessionStorage, saved login state.

Tests that come from manual test cases carry the case number in their parameters (`TC-016`, `TC-020`, etc.).

## Known site bugs

Tests for found bugs are written with the **correct** expected result and marked
`xfail` with the bug number (for example, `BUG-012`). When a bug is fixed, pytest reports
that the test unexpectedly passed, and the mark can be removed.

## Reports and diagnostics

- Full-page screenshots and traces are saved only for failed tests (the `test-results/` folder).
- Open a trace: `playwright show-trace path/to/trace.zip`.
- In GitHub Actions the `report.html` report and the files of failed tests are saved as artifacts
  for 7 days (the run page, the **Artifacts** block).
