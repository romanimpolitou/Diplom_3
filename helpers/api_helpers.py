import random

import allure
import requests

from constants import MAIN_PAGE_URL


def generate_user():
    email = f"romanimpolitov50{random.randint(100, 999)}@yandex.ru"
    password = "qwerty"
    name = "Roman"
    return {"name": name, "email": email, "password": password}


@allure.step("Регистрация нового пользователя")
def create_user(api_client):
    user_data = generate_user()
    response = api_client.post("/api/auth/register", json=user_data)
    token = response.json().get("accessToken")
    return token, user_data


@allure.step("Удаление пользователя")
def delete_user(token):
    headers = {"Authorization": token}
    return requests.delete(f"{MAIN_PAGE_URL}/api/auth/user", headers=headers)


@allure.step("Создание заказа")
def create_order(token, ingredients):
    headers = {"Authorization": token}
    payload = {"ingredients": ingredients}
    response = requests.post(f"{MAIN_PAGE_URL}/api/orders", json=payload, headers=headers)
    return response


