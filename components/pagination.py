import re
class Pagination:
    def __init__(self, page):
        self.root = page.locator("my-pager")
        self.previous_button = self.root.locator('a.btn', has_text='«')
        self.next_button = self.root.locator('a.btn', has_text='»')
        self.page_input = self.root.locator('input')
        self.page_info = self.root.get_by_text(re.compile(r'page \d+ of \d+'))

    def next(self):
        self.next_button.click()

    def previous(self):
        self.previous_button.click()
