from pages.base_page import BasePage
from components.button import Button
from components.fill import Fill


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = Fill(page.locator("#user-name"), "Username field")
        self.password_input = Fill(page.locator("#password"), "Password field")
        self.login_button = Button(page.get_by_role("button", name="Login"), "User name Field")

    def login(self, username, password):
        self.username_input.clear_fill(username)
        self.password_input.clear_fill(password)
        self.login_button.single_click()
