from .base_page import BasePage

class CommunityPage(BasePage):
    #https://playwright.dev/python/docs/test-runners#configure-base-url
    url = "https://sport.mos.ru/community/XrqQBLk9oV"

    def navigate(self):
        self.page.goto(self.url)

    def apply_request(self):
        #Абсолютные локаторы зло
        self.page.locator("xpath=//*[@id='root']/div[1]/main/div[1]/div/div[2]/div[2]/div/div[2]/button[1]").wait_for()
        self.page.locator("xpath=//*[@id='root']/div[1]/main/div[1]/div/div[2]/div[2]/div/div[2]/button[1]").click()

    def confirm_request(self):
        self.page.locator("xpath=/html/body/div[3]/div[3]/div/div/div[2]/button[1]").wait_for()
        self.page.locator("xpath=/html/body/div[3]/div[3]/div/div/div[2]/button[1]").click()

    def done_request(self):
        self.page.locator("xpath=/html/body/div[3]/div[3]/div/div/div/div/div[2]/button").wait_for()
        self.page.locator("xpath=/html/body/div[3]/div[3]/div/div/div/div/div[2]/button").click()

    def open_menu(self):
        self.page.locator("xpath=//*[@id='root']/div[1]/header/div/div/div/div[3]/button[2]").wait_for()
        self.page.locator("xpath=//*[@id='root']/div[1]/header/div/div/div/div[3]/button[2]").click()

    def logout(self):
        self.page.locator("xpath=//p[contains(text(), 'Выйти из профиля')]").wait_for()
        self.page.locator("xpath=//p[contains(text(), 'Выйти из профиля')]").click()