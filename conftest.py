import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from constants import MAIN_PAGE_URL
from helpers.api_helpers import create_user, delete_user


@pytest.fixture
def api_client():
    class APIClient:
        def post(self, endpoint, json=None):
            url = f"{MAIN_PAGE_URL}{endpoint}"
            return requests.post(url, json=json)
    return APIClient()


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.get(MAIN_PAGE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def auth_user(api_client):
    token, user_data = create_user(api_client)
    try:
        yield token, user_data
    finally:
        if token:
            try:
                delete_user(token)
            except Exception as e:
                print(f"Не удалось удалить тестового пользователя: {e}")