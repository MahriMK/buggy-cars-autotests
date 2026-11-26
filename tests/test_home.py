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

# ТС-037-040
def test_card_image_opens_page(home_page, page):
    home_page.open()
    home_page.card("Overall Rating").image.click()
    expect(page).to_have_url('/overall')

@pytest.mark.xfail(raises=AssertionError, reason="BUG-005: card title is not a link")
def test_card_title_opens_page(home_page, page):
    home_page.open()
    home_page.card('Overall Rating').title.click()
    expect(page).to_have_url("/overall")

@pytest.mark.xfail(reises=AssertionError, reason="BUG-006: card description is not a link")
def test_card_description_opens_page(home_page, page):
    home_page.open()
    home_page.card("Overall Rating").description.click()
    expect(page).to_vahe_url('/overall')

@pytest.mark.xfail(raises=AssertionError, reason="BUG-007: free area of the card is not a link")
def test_card_free_area_opens_page(home_page, page):
    home_page.open()
    home_page.card("Overall Rating").description.click(position={"x":3, "y":3})
    expect(page).to_have_url('/overall')