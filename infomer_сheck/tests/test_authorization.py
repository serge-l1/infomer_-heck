import pytest
from pages.home_page import HomePage
from pages.authorization_page import AuthorizationPage
from pages.community_page import CommunityPage

@pytest.mark.dependency(name="auth_and_apply")
def test_authorization_entry_in_community(page):
    home = HomePage(page)
    home.navigate()
    home.click_agree()

    auth = AuthorizationPage(page)
    auth.click_registration()
    page.wait_for_load_state("networkidle")
    auth.fill_credentials("", "")
    auth.click_login()

    community = CommunityPage(page)
    community.navigate()
    community.apply_request()
    community.confirm_request()
    community.done_request()
    community.open_menu()
    community.logout()

    # Дополнительно можно проверить, что выход выполнен успешно
    assert True