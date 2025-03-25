from .base_page import BasePage

class AccountPage(BasePage):
    def click_change_account_icon(self):
        #Писать ожидание локатора не нужно. https://playwright.dev/python/docs/actionability
        self.page.locator("xpath=//*[@id='other-user']/div/div[2]/button/div/svg/path").wait_for()
        #Старайся не использовать абсолютный xpath путь 
        self.page.locator("xpath=//*[@id='other-user']/div/div[2]/button/div/svg/path").click()

    def click_login_another_account(self):
        self.page.locator("xpath=//*[@id='mus-selector']/section/div/div[2]/button/div/p").wait_for()
        self.page.locator("xpath=//*[@id='mus-selector']/section/div/div[2]/button/div/p").click()