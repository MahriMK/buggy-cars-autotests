import re
import pytest
from playwright.sync_api import expect

def test_profile_and_logout_visible_after_login(logged_in_page, header):
    expect(header.profile_link).to_be_visible()
    expect(header.logout_link).to_be_visible()

def test_open_profile_page(logged_in_page, header):
    header.open_profile()
    expect(logged_in_page).to_have_url(re.compile(r'/profile$'))

def test_logout_shows_login_form_again(logged_in_page, header):
    header.logout()
    expect(header.login_button).to_be_visible()

def test_login_with_wrong_password_shows_error(home_page, test_data):
    home_page.open()
    home_page.header.login(test_data['username'], "Wrong123!")
    expect(home_page.header.invalid_credentials_error).to_be_visible()

def test_login_with_unknown_username_shows_error(home_page, test_data):
    home_page.open()
    home_page.header.login("nouser-99999", test_data['password'])
    expect(home_page.header.invalid_credentials_error).to_be_visible()

@pytest.mark.parametrize("username_template, password_template", [
    (" {}", "{}"),
    ("{} ", "{}"),
    ("{}", " {}"),
    ("{}", "{} "),
], ids=["TC-028", "TC-029", "TC-030", "TC-031"])
def test_login_with_extra_space_shows_error(home_page, test_data, username_template, password_template):
    home_page.open()
    home_page.header.login(
        username_template.format(test_data['username']),
        password_template.format(test_data["password"])
    )
    expect(home_page.header.invalid_credentials_error).to_be_visible()

 