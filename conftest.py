import os

import pytest
from playwright.sync_api import expect
from pages.register_page import RegisterPage
from pages.home_page import HomePage
from components.header import Header


@pytest.fixture(scope="session")
def test_data():
    return {
        'username': 'user1221',
        'password': 'johNny123!'
    }


def log_in(page, test_data):
    """Open the home page and log in through the Header component."""
    page.goto("/")
    Header(page).login(test_data['username'], test_data['password'])
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

@pytest.fixture
def register_page(page):
    return RegisterPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def header(page):
    return Header(page)