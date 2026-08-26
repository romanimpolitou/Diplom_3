import allure

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


@allure.feature("Конструктор")
class TestConstructor:

    @allure.story("Переход по клику на 'Конструктор'")
    def test_click_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_orders()
        main_page.click_to_constructor()
        assert main_page.check_element_visibility(MainPageLocators.header1)


    @allure.story("Переход по клику на раздел 'Лента заказов'")
    def test_click_to_orders(self, driver):
        main_page = MainPage(driver)
        main_page.click_top_orders()
        assert main_page.check_element_visibility(MainPageLocators.header2)


    @allure.story("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        assert main_page.modal_window_open()


    @allure.story("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_ingredient()
        main_page.close_modal_window()
        assert main_page.modal_window_closed()


    @allure.story("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        quantity = main_page.get_ingredient_counter()
        main_page.drag_ingredient()
        new_quantity = main_page.get_ingredient_counter()
        assert int(quantity) < int(new_quantity)