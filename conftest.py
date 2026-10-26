import os

import pytest
from playwright.sync_api import expect


@pytest.fixture
def test_data():
     return {
        'username': 'user1221',
        'password': 'johNny123!'
    }


def log_in(page, test_data):
    """Fill the login form on the home page and submit it."""
    page.goto("/")
    page.locator('input[name="login"]').fill(test_data["username"])
    page.locator('input[name="password"]').fill(test_data["password"])
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Logout")).to_be_visible()


@pytest.fixture
def logged_in_page(page, test_data):
    """A page where the user is already logged in."""
    log_in(page, test_data)
    return page


@pytest.fixture(scope="session")
def auth_state(browser, base_url, test_data, tmp_path_factory):
    """Log in once and save the session to a temporary file (not stored in the repo)."""
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    log_in(page, test_data)
    path = tmp_path_factory.mktemp("auth") / "auth.json"
    context.storage_state(path=str(path))
    context.close()
    return str(path)
