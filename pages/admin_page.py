import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    PATH = "/administration"
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_FORM_SUBMIT_BUTTON = (By.XPATH, '//*[@id="form-login"]/div[3]/button')
    LOGOUT_LINK = (By.XPATH, '//*[@id="nav-logout"]/a')
    # NAVIGATION
    CATALOG_MENU_LINK = (By.LINK_TEXT, "Catalog")
    CATALOG_PRODUCTS_MENU_LINK = (By.LINK_TEXT, "Products")

    def open(self):
        with allure.step(f"Открываем страницу {self.browser.url + self.PATH}"):
            self.browser.get(self.browser.url + self.PATH)

    @allure.step("Вводим в поле Username '{username}'")
    def enter_username(self, username):
        self.enter_value(self.USERNAME_INPUT, username)

    @allure.step("Вводим в поле Password '{password}'")
    def enter_password(self, password):
        self.enter_value(self.PASSWORD_INPUT, password)

    @allure.step("Нажимаем на кнопку 'Login'")
    def submit_form(self):
        self.click(self.LOGIN_FORM_SUBMIT_BUTTON)

    @allure.step("Проверяем наличие ссылки 'Logout'")
    def logout_link_is_present(self):
        return self.get_element(self.LOGOUT_LINK)

    @allure.step("Нажимаем на ссылку 'Logout'")
    def click_logout_link(self):
        self.click(self.LOGOUT_LINK)

    @allure.step("Проверяем наличие кнопки 'Login'")
    def login_button_is_present(self):
        return self.get_element(self.LOGIN_FORM_SUBMIT_BUTTON)

    @allure.step("Переходим в раздел 'Catalog' - 'Products'")
    def navigate_to_catalog_products(self):
        self.click(self.CATALOG_MENU_LINK)
        self.click(self.CATALOG_PRODUCTS_MENU_LINK)
