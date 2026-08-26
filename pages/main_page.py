import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Конструктор' в шапке")
    def click_to_constructor(self):
        self.click_on_element(MainPageLocators.top_constructor_button)


    @allure.step("Клик по ингредиенту")
    def click_to_ingredient(self):
        self.click_on_element(MainPageLocators.ingredient)


    @allure.step("Перетащить ингредиент в поле конструктора")
    def drag_ingredient(self):
        self.drag_and_drop(MainPageLocators.ingredient, MainPageLocators.constructor_field)


    @allure.step("Посмотреть счётчик ингредиента")
    def get_ingredient_counter(self):
        return self.text_of_element(MainPageLocators.counter)


    @allure.step("Клик по кнопке 'Лента заказов' в шапке")
    def click_top_orders(self):
        try:
            self.click_on_element(MainPageLocators.close_modal_button)
        except Exception:
            pass
        self.click_on_element(MainPageLocators.top_orders_button)


    @allure.step("Посмотреть счётчик 'Выполнено за всё время'")
    def get_all_orders_counter(self):
        return self.text_of_element(MainPageLocators.all_orders)


    @allure.step("Посмотреть счётчик 'Выполнено за сегодня'")
    def get_today_orders_counter(self):
        return self.text_of_element(MainPageLocators.today_orders)


    @allure.step("Посмотреть номер заказа в разделе 'В работе'")
    def get_order_in_progress(self, order_number, timeout=5):
        locator = (By.XPATH, f"//p[text()='{order_number}']")
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except:
            return None


    @allure.step("Проверить наличие модального окна")
    def modal_window_open(self):
        return self.find_element(MainPageLocators.modal_window).is_displayed()


    @allure.step("Нажать на крестик на модальном окне")
    def close_modal_window(self):
        self.click_on_element(MainPageLocators.close_modal_button)
        self.wait.until(EC.invisibility_of_element_located(MainPageLocators.modal_window))


    @allure.step("Проверить, что модальное окно закрыто")
    def modal_window_closed(self):
        try:
            return not self.find_element(MainPageLocators.modal_window).is_displayed()
        except Exception:
            return True