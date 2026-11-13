import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
def test_homepage_title(home_page, page):
    home_page.open()
    expect(page).to_have_title('Buggy Cars Rating')

@pytest.mark.smoke
def test_homepage_heading_visible(home_page):
    home_page.open()
    expect(home_page.heading).to_be_visible()

@pytest.mark.regression
def test_popular_make_visible(home_page):
    home_page.open()
    expect(home_page.popular_make).to_be_visible()

@pytest.mark.regression
def test_overall_rating_heading(home_page):
    home_page.open()
    expect(home_page.overall_rating_heading).to_be_visible()
    expect(home_page.overall_rating_heading).to_have_text('Overall Rating')

def test_login_and_register_controls_visible(home_page):
    home_page.open()
    expect(home_page.header.login_button).to_be_visible()
    expect(home_page.header.register_link).to_be_visible