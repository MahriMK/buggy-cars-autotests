class Header:
    def __init__(self, page):
        self.root = page.locator('nav.navbar')
        self.logo = self.root.locator('a.navbar-brand')
        self.login_input = self.root.locator('input[name="login"]')
        self.password_input = self.root.locator('input[name="password"]')
        self.login_button = self.root.get_by_role('button', name='Login')
        self.register_link = self.root.get_by_role('link', name='Register')

    def login(self, username, password):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()