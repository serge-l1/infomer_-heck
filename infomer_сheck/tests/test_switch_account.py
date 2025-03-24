import pytest
from pages.authorization_page import AuthorizationPage
from pages.account_page import AccountPage
from pages.messages_page import MessagesPage

@pytest.mark.dependency(depends=["auth_and_apply"])
def test_login_with_another_account(page):
    # Обеспечиваем, что страница загружена и кликабельна
    # Если страница оказалась about:blank, выполняем переход на базовый URL
    page.goto("https://sport.mos.ru/")
    page.wait_for_load_state("networkidle")
    
    # Далее стандартные действия второго теста
    auth = AuthorizationPage(page)
    auth.click_registration()
    page.wait_for_load_state("networkidle")
    
    account = AccountPage(page)
    account.click_change_account_icon()
    account.click_login_another_account()

    auth.fill_credentials("", "")
    auth.click_login()

    messages = MessagesPage(page)
    messages.navigate()

    # Добавьте необходимые проверки, например:
    assert page.url.startswith("https://sport.mos.ru/messages")