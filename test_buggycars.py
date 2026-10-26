import re

import pytest
from playwright.sync_api import expect


# ---------- Home page ----------

@pytest.mark.smoke
def test_homepage_title(page):
    page.goto("/")
    expect(page).to_have_title("Buggy Cars Rating")


@pytest.mark.smoke
def test_homepage_heading_visible(page):
    page.goto("/")
    expect(page.get_by_role("heading", name="Buggy Cars Rating")).to_be_visible()


@pytest.mark.regression
def test_popular_make_visible(page):
    page.goto("/")
    expect(page.get_by_text("Popular Make")).to_be_visible()


@pytest.mark.regression
def test_overall_rating_heading(page):
    page.goto("/")
    heading = page.get_by_role("heading", name="Overall Rating")
    expect(heading).to_be_visible()
    expect(heading).to_have_text("Overall Rating")


def test_login_and_register_controls_visible(page):
    page.goto("/")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    expect(page.get_by_role("link", name="Register")).to_be_visible()


# ---------- Registration ----------

def test_register_link_opens_registration_page_regex(page):
    page.goto("/")
    page.get_by_role("link", name="Register").click()
    # Variant 1: regular expression. Matches any address that ends with /register,
    # so the test does not depend on the domain. "$" means "end of the string".
    expect(page).to_have_url(re.compile(r"/register$"))

def test_register_link_opens_registration_page_exact_url(page):
    page.goto("/")
    page.get_by_role("link", name="Register").click()
    # Variant 2: exact address. Stricter and easier to read,
    # but it must be changed if the site moves to another domain.
    expect(page).to_have_url("https://buggy.justtestit.org/register")


def test_register_cancel_returns_to_home_regex(page):
    page.goto("/register")
    page.get_by_role("button", name="Cancel").click()
    # Variant 1: regular expression. Matches any address that ends with "/",
    # which is how the home page address looks. "$" means "end of the string".
    expect(page).to_have_url(re.compile(r"/$"))

def test_register_cancel_returns_to_home_exact_url(page):
    page.goto("/register")
    page.get_by_role("button", name="Cancel").click()
    # Variant 2: exact address of the home page. Stricter and easier to read,
    # but it must be changed if the site moves to another domain.
    expect(page).to_have_url("https://buggy.justtestit.org/")


@pytest.mark.parametrize("firstname, lastname", [
    ("Anna", "Smith"),
    ("John", "Brown"),
    ("Bill", "Taylor"),
])
def test_register_name_fields_accept_input(page, firstname, lastname):
    page.goto("/register")
    page.locator("#firstName").fill(firstname)
    page.locator("#lastName").fill(lastname)
    expect(page.locator("#firstName")).to_have_value(firstname)
    expect(page.locator("#lastName")).to_have_value(lastname)


def test_register_with_existing_username_shows_error(page):
    # Relies on the user "anna-lambo" already existing on the site.
    page.goto("/register")
    page.locator("#username").fill("anna-lambo")
    page.locator("#firstName").fill("Anna")
    page.locator("#lastName").fill("Smith")
    page.locator("#password").fill("Qwerty123!")
    page.locator("#confirmPassword").fill("Qwerty123!")
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_text("UsernameExistsException: User already exists")).to_be_visible()


# ---------- Login / logout ----------

def test_profile_and_logout_visible_after_login(logged_in_page):
    expect(logged_in_page.get_by_role("link", name="Profile")).to_be_visible()
    expect(logged_in_page.get_by_role("link", name="Logout")).to_be_visible()


def test_open_profile_page(logged_in_page):
    logged_in_page.get_by_role("link", name="Profile").click()
    expect(logged_in_page).to_have_url(re.compile(r"/profile$"))


def test_logout_shows_login_form_again(logged_in_page):
    logged_in_page.get_by_role("link", name="Logout").click()
    expect(logged_in_page.get_by_role("button", name="Login")).to_be_visible()


# ---------- Pagination ----------

def test_pagination_next_button_opens_page_2_regex(page):
    page.goto("/")
    page.locator('a[href="/overall"]').click()
    # Variant 1: regular expression, "$" means "end of the string".
    expect(page).to_have_url(re.compile(r"/overall$"))
    page.get_by_text("»").click()
    # A pattern is used on purpose: the total number of pages can change.
    expect(page.get_by_text(re.compile(r"page 2 of \d+"))).to_be_visible()


def test_pagination_next_button_opens_page_2_exact_url(page):
    page.goto("/")
    page.locator('a[href="/overall"]').click()
    # Variant 2: exact address. Stricter, but depends on the domain.
    expect(page).to_have_url("https://buggy.justtestit.org/overall")
    page.get_by_text("»").click()
    expect(page.get_by_text(re.compile(r"page 2 of \d+"))).to_be_visible()


# ---------- Saved authorization state ----------

def test_profile_visible_with_saved_auth_state(browser, base_url, auth_state):
    context = browser.new_context(storage_state=auth_state, base_url=base_url)
    page = context.new_page()
    page.goto("/")
    expect(page.get_by_role("link", name="Profile")).to_be_visible()
    context.close()


def test_login_form_visible_without_auth_state(browser, base_url):
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/")
    expect(page.get_by_role("button", name="Login")).to_be_visible()
    context.close()


# ---------- Cookies and browser storage ----------

def test_add_cookie(page, context):
    page.goto("/")
    context.add_cookies([
        {"name": "test_cookie", "value": "123", "domain": "buggy.justtestit.org", "path": "/"}
    ])
    cookie = next((c for c in context.cookies() if c["name"] == "test_cookie"), None)
    assert cookie is not None, "test_cookie was not added"
    assert cookie["value"] == "123"


def test_clear_cookies(page, context):
    page.goto("/")
    context.add_cookies([
        {"name": "test_cookie", "value": "123", "domain": "buggy.justtestit.org", "path": "/"}
    ])
    assert any(c["name"] == "test_cookie" for c in context.cookies())
    context.clear_cookies()
    assert context.cookies() == []


@pytest.mark.parametrize("storage", ["localStorage", "sessionStorage"])
def test_browser_storage_set_and_remove(page, storage):
    page.goto("/")
    page.evaluate(f"{storage}.setItem('test_key', '123')")
    assert page.evaluate(f"{storage}.getItem('test_key')") == "123"
    page.evaluate(f"{storage}.removeItem('test_key')")
    assert page.evaluate(f"{storage}.getItem('test_key')") is None
