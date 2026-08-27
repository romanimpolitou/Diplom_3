import time

import allure

from helpers.api_helpers import create_order
from pages.main_page import MainPage


@allure.feature("Счётчики в разделе 'Лента заказов")
class TestOrdersPage:

    @allure.story("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    @allure.title("Счётчик 'Выполнено за всё время' увеличивается при создании заказа")
    def test_all_orders_counter(self, driver, auth_user):
        token, _ = auth_user

        with allure.step("Перейти в раздел 'Лента заказов"):
            main_page = MainPage(driver)
            main_page.click_top_orders()

        with allure.step("Получить текущее значение счётчика 'Выполнено за всё время'"):
            quantity = int(main_page.get_all_orders_counter())

        with allure.step("Создать заказ с ингредиентами"):
            ingredients = ["61c0c5a71d1f82001bdaaa6d"]
            create_order(token, ingredients)

        start = time.time()
        timeout = 30
        new_quantity = quantity

        while time.time() - start < timeout:
            new_quantity = int(main_page.get_all_orders_counter())
            if new_quantity > quantity:
                break
            time.sleep(1)

        with allure.step("Проверка, что счётчик увеличился"):
            assert new_quantity > quantity


    @allure.story("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается при создании заказа")
    def test_today_orders_counter(self, driver, auth_user):
        token, _ = auth_user
    
        with allure.step("Перейти в раздел 'Лента заказов"):
            main_page = MainPage(driver)
            main_page.click_top_orders()
    
        with allure.step("Получить текущее значение счётчика 'Выполнено за всё время'"):
            quantity = int(main_page.get_today_orders_counter())
    
        with allure.step("Создать заказ с ингредиентами"):
            ingredients = ["61c0c5a71d1f82001bdaaa6d"]
            create_order(token, ingredients)
    
        start = time.time()
        timeout = 30
        new_quantity = quantity

        while time.time() - start < timeout:
            new_quantity = int(main_page.get_today_orders_counter())
            if new_quantity > quantity:
                break
            time.sleep(1)
    
        with allure.step("Проверка, что счётчик увеличился"):
            assert new_quantity > quantity


    @allure.story("Номер заказа появляется в разделе 'В работе'")
    @allure.title("Номер заказа отображается в разделе 'В работе' после создания")
    def test_order_number_in_progress(self, driver, auth_user):
        token, _ = auth_user

        with allure.step("Создать заказ"):
            ingredient = ["61c0c5a71d1f82001bdaaa6d"]
            response = create_order(token, ingredient)
            order_number = response.json()["order"]["number"]

        with allure.step("Перейти в раздел 'Лента заказов"):
            main_page = MainPage(driver)
            main_page.click_top_orders()

        with allure.step("Ждать появления заказа в ленте"):
            order_in_progress = main_page.get_order_in_progress(order_number)

        with allure.step("Проверить номер заказа"):
            assert order_in_progress is not None, f"Заказ №{order_number} не найден в ленте"