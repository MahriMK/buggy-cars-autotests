from playwright.sync_api import expect
import pytest

def test_register_cancel_returns_to_home(register_page, page):
    register_page.open()
    register_page.cancel()
    expect(page).to_have_url("https://buggy.justtestit.org/")

def test_register_with_existing_username_shows_error(register_page):
    register_page.open()
    register_page.fill_form('anna-lambo', 'Anna', 'Smith', 'Qwerty123!')
    register_page.submit()
    expect(register_page.username_exists_error).to_be_visible()

@pytest.mark.parametrize('firstname, lastname', [
    ('Anna', 'Smith'),
    ('John', 'Brown'),
    ('Bill', 'Taylor'),
])
def test_register_name_fields_accept_input(register_page, firstname, lastname):
    register_page.open()
    register_page.first_name.fill(firstname)
    register_page.last_name.fill(lastname)
    expect(register_page.first_name).to_have_value(firstname)
    expect(register_page.last_name).to_have_value(lastname)

def test_register_link_opens_registration_page(home_page, page):
    home_page.open()
    home_page.open_register_page()
    expect(page).to_have_url("https://buggy.justtestit.org/register")

def test_register_with_mismatched_passwords_shows_error(register_page):
    register_page.open()
    register_page.fill_form(
        "test-mismatch-user",
        "Anna",
        "Smith",
        "Qwerty123!",
        "Different1!"
        )
    expect(register_page.password_mismatch_error).to_be_visible()
    expect(register_page.register_button).to_be_disabled()