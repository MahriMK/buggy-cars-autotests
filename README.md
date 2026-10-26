# qa-project

UI test automation for the demo site [Buggy Cars Rating](https://buggy.justtestit.org).
Written with Python, Pytest and Playwright.

## What is covered
- Home page: title, headings, main controls
- Registration: form fields, cancel button, error for an existing username
- Login and logout, profile page
- Pagination
- Saved authorization state (`storage_state`)
- Cookies, localStorage and sessionStorage

## Setup
```bash
pip install -r requirements.txt
playwright install
```


## Run
```bash
pytest                  # all tests
pytest -m smoke         # only smoke tests
pytest --headed         # watch the browser
```

## Structure
- `test_buggycars.py` - tests
- `conftest.py` - fixtures (login, saved auth state, test data)
- `pytest.ini` - base URL and test markers
- `requirements.txt` - dependencies
- `.gitignore` - files excluded from the repository



## Notes
- The test for an existing username expects the user `anna-lambo` to already exist on the demo site.
- Markers `smoke` and `regression` are set only on part of the tests; unmarked tests run with plain `pytest`.