import pytest
from playwright.sync_api import expect

@pytest.mark.parametrize("path", [
     "/overall",
    "/model/ckl2phsabijs71623vk0%7Cckl2phsabijs71623vqg",
], ids=["TC-050-overall-rating", "TC-047-popular-model"])
def test_logo_click_opens_home_page(page, header, path):
    page.goto(path)
    header.logo.click()
    expect(page).to_have_url('/')

@pytest.mark.xfail(reason="BUG-008: logo on Popular Make page does not open the home page")
def test_logo_click_on_popular_make_opens_home_page(page, header, path):
    page.goto(path)
    header.logo.click()
    expect(page).to_have_url('/')