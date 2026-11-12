class LoginPage:
    def __init__(self, page):
        self.page = page
    def open(self, base_url):
        self.page.goto(base_url + "/index.html")
        return self
    def login(self):
        self.page.get_by_role("button", name="Login").click()
        return self
    @property
    def welcome_message(self):
        return self.page.locator("#auth-status")
