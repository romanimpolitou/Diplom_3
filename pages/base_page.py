import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import DRAG_AND_DROP_SCRIPT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step("Дождаться видимости элемента на странице")
    def waiting_for_element_visible(self, locator, timeout = 10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))


    @allure.step("Проверка отображения элемента на странице")
    def check_element_visibility(self, locator):
        elmnt = self.waiting_for_element_visible(locator)
        return elmnt.is_displayed()


    @allure.step("Дождаться кликабельности элемента")
    def waiting_for_element_clickable(self, locator, timeout = 10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))


    @allure.step("Получить текст элемента")
    def text_of_element(self, locator):
        elmnt = self.waiting_for_element_visible(locator)
        return elmnt.text


    @allure.step("Нажать на элемент")
    def click_on_element(self, locator, timeout = 10):
        elmnt = self.waiting_for_element_clickable(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", elmnt)
        elmnt.click()


    @allure.step("Найти один элемент")
    def find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))


    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source, target):
        self.wait.until(EC.presence_of_element_located(source))
        self.wait.until(EC.presence_of_element_located(target))
        drag_from = self.driver.find_element(*source)
        drag_to = self.driver.find_element(*target)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, drag_from, drag_to)


    @allure.step("Дождаться увеличения значения элемента")
    def wait_until_value_increases(self, locator, old_value, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(lambda d: int(d.find_element(*locator).text) > int(old_value))