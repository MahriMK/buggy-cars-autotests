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

@pytest.mark.parametrize("password, error_text",[
    ("pass12", "Password not long enough"),
    ("12345678", "must have lowercase characters"),
    ("password", "must have uppercase characters"),
    ("Password", "must have numeric characters"),
    ("Password1", "must have symbol characters") 
], ids=["TC-016", "TC-017", "TC-018", "TC-019", "TC-020"])
def test_register_with_invalid_password_shows_error(register_page, password, error_text):
    register_page.open()
    register_page.fill_form("test-invalid-pass", "Anna", "Smith", password)
    register_page.submit()
    expect(register_page.error_with_text(error_text)).to_be_visible()

@pytest.mark.parametrize("username, first_name, last_name, password, confirm_password", [
    ("", "Anna", "Smith", "Qwerty123!", "Qwerty123!"),
("test-empty-field", "", "Smith", "Qwerty123!", "Qwerty123!"),
("test-empty-field", "Anna", "", "Qwerty123!", "Qwerty123!"),
("test-empty-field", "Anna", "Smith", "Qwerty123!", ""),
], ids=["TC-006-login", "TC-010-first-name", "TC-013-last-name", "TC-021-confirm-password"])
def test_register_button_disabled_when_required_field_is_empty(
    register_page, username, first_name, last_name, password, confirm_password
):
    register_page.open()
    register_page.fill_form(username, first_name, last_name, password, confirm_password)
    expect(register_page.register_button).to_be_disabled()