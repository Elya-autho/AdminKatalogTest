from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import allure


class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH,"(//input[@placeholder='Логин'])")
    PASSWORD_FIELD = (By.XPATH,"(//input[@placeholder='Пароль'])")
    BUTTON_SEND = (By.XPATH,"(//*[@class='block'])")



class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.BUTTON_SEND)

    @allure.step("Заполняем поле логин")
    def type_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Заполняем поле пароля")
    def type_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Нажимаем на кнопку Войти")
    def click_login(self):
        self.attach_screenshot()
        button_login = self.find_element(LoginPageLocators.BUTTON_SEND)
        button_login.click()
