class HomePage:
    def __init__(self, page):
        self.page = page
        self.register_link = page.get_by_role('link', name='Register')

    def open(self):
        self.page.goto('/')

    def open_register_page(self):
        self.register_link.click()