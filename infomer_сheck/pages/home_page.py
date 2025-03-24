from .base_page import BasePage

class HomePage(BasePage):
    url = "https://sport.mos.ru/"

    def navigate(self):
        self.page.goto(self.url)

    def click_agree(self):
        self.page.locator("button:has-text('Согласен')").click()