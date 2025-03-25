import pytest
from playwright.sync_api import sync_playwright

#Тут описать фикстуры для POM
#https://dev.to/lrenzi/playwright-with-python-a-quick-guide-356p

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(autouse=True)
def before_each(page):
    #base url спрятать в https://pypi.org/project/python-dotenv/
    page.goto("https://sport.mos.ru/")