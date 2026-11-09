from playwright.sync_api import expect

def test_register_cancel_returns_to_home(register_page, page):
    register_page.open()
    register_page.cancel()
    expect(page).to_have_url("https://buggy.justtestit.org/")

def test_register_with_existing_username_shows_error(register_page, page):
    register_page.open()
    register_page.fill_form('anna-lambo', 'Anna', 'Smith', 'Qwerty123!')
    register_page.submit()
    expect(register_page.username_exists_error).to_be_visible()