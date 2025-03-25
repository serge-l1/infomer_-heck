from .base_page import BasePage

class AuthorizationPage(BasePage):
    def click_registration(self):
        #Лучше испольщовать ARIA ROLE
        self.page.get_by_role('button', name="РЕГИСТРАЦИЯ")
        #self.page.locator("button:has-text('РЕГИСТРАЦИЯ')").click()

    def fill_credentials(self, login: str, password: str):
        #Ожидать не нужно
        self.page.locator("#login").wait_for()
        self.page.locator("#login").fill(login)
        self.page.locator("#password").wait_for()
        self.page.locator("#password").fill(password)

    def click_login(self):
         #Лучше испольщовать ARIA ROLE
        self.page.locator("button#bind:has-text('Войти')").click()