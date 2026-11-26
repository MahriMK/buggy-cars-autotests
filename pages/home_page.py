from components.header import Header
from components.card import Card

class HomePage:
    def __init__(self, page):
        self.page = page
        self.header = Header(page)
        self.cards = page.locator('div.card')
        self.heading = page.get_by_role('heading', name='Buggy Cars Rating')
        self.popular_make = page.get_by_text('Popular Make')
        self.overall_rating_heading = page.get_by_role('heading', name='Overall Rating')

    def open(self):
        self.page.goto('/')

    def open_register_page(self):
        self.header.register_link.click()

    def card(self, title):
        return Card(self.cards.filter(has_text=title))