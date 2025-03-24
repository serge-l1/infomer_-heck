from .base_page import BasePage

class MessagesPage(BasePage):
    url = "https://sport.mos.ru/messages?message_type=Unread"

    def navigate(self):
        self.page.goto(self.url)