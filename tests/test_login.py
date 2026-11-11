import re
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