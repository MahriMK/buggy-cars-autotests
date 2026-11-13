import pytest
from playwright.sync_api import expect

def test_next_button_opens_page_2(overall_rating_page):
    overall_rating_page.open()
    overall_rating_page.pagination.next()
    expect(overall_rating_page.pagination.page_info).to_contain_text('page 2 of 5')

@pytest.mark.xfail(reason='BUG-012: Next button stays active on the last page')
def test_next_on_last_page_stays_on_last_page(overall_rating_page):
    pagination = overall_rating_page.pagination
    overall_rating_page.open()
    for page_number in range(2,6):
        pagination.next()
        expect(pagination.page_info).to_contain_text(f"page {page_number} of 5")
    pagination.next()
    expect(pagination.page_info).to_contain_text('page 5 of 5')

