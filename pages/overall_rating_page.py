from components.pagination import Pagination

class OverallRatingPage:
    def __init__(self, page):
        self.page = page
        self.pagination = Pagination(page)

    def open(self):
        self.page.goto('/overall')
