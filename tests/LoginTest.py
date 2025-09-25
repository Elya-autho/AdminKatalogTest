from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import time
import allure

BASE_URL = 'https://test-admin.retail-kb.kbapp.ru/login'
OPEN_ADMIN = 'https://test-admin.retail-kb.kbapp.ru/'

LOGIN = "admin"
PASSWORD = "nanotek24"
time_sleep = 2

@allure.story("Проверка авторизации и входа в приложение")
def test_authorisation(browser):
    with allure.step("Открываем страницу"):
        BasePage(browser).get_url(BASE_URL)
    with allure.step("Создаем объект страницы"):
        input_login = LoginPageHelper(browser)
    with allure.step("Вводим логин"):
        input_login.type_login(LOGIN)

    time.sleep(time_sleep)
    with allure.step("Создаем объект страницы"):
        input_password = LoginPageHelper(browser)
    with allure.step("Вводим пароль"):
        input_password.type_password(PASSWORD)
    time.sleep(time_sleep)
    with allure.step("Создаем объект страницы"):
        send_button = LoginPageHelper(browser)
    with allure.step("Нажимаем на кнопку Войти"):
        send_button.click_login()
    time.sleep(time_sleep * 25)
