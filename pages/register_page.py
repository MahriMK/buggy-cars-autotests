class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator('#username')
        self.first_name = page.locator('#firstName')
        self.last_name = page.locator('#lastName')
        self.password = page.locator('#password')
        self.confirm_password = page.locator('#confirmPassword')
        self.register_button = page.get_by_role('button', name='Register')
        self.cancel_button = page.get_by_role('button', name="Cancel")
        self.username_exists_error = page.get_by_text('UsernameExistsException: User already exist')

    def open(self):
        self.page.goto('/register')

    def fill_form(self, username, first_name, last_name, password, confirm_password=None):
        self.username.fill(username)
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.password.fill(password)
        self.confirm_password.fill(confirm_password if confirm_password is not None else password)

    def submit(self):
        self.register_button.click()

    def cancel(self):
        self.cancel_button.click()
