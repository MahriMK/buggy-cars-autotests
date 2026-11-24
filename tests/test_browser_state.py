import pytest
from playwright.sync_api import expect


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