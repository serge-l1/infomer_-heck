from .base_page import BasePage

class AuthorizationPage(BasePage):
    def click_registration(self):
        self.page.locator("button:has-text('РЕГИСТРАЦИЯ')").click()

    def fill_credentials(self, login: str, password: str):
        self.page.locator("#login").wait_for()
        self.page.locator("#login").fill(login)
        self.page.locator("#password").wait_for()
        self.page.locator("#password").fill(password)

    def click_login(self):
        self.page.locator("button#bind:has-text('Войти')").click()