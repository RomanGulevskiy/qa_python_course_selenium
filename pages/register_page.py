import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    FIRSTNAME_INPUT = (By.NAME, "firstname")
    LASTNAME_INPUT = (By.NAME, "lastname")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    POLICY_CHECKBOX = (By.NAME, "agree")
    REGISTER_FORM_SUBMIT_BUTTON = (By.XPATH, '//*[@id="form-register"]/div/button')
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def open(self):
        with allure.step(f"Открываем страницу {self.browser.url + self.PATH}"):
            self.browser.get(self.browser.url + self.PATH)

    @allure.step("Вводим в поле First Name '{firstname}'")
    def enter_firstname(self, firstname):
        self.enter_value(self.FIRSTNAME_INPUT, firstname)

    @allure.step("Вводим в поле Last Name '{lastname}'")
    def enter_lastname(self, lastname):
        self.enter_value(self.LASTNAME_INPUT, lastname)

    @allure.step("Вводим в поле E-Mail '{email}'")
    def enter_email(self, email):
        self.enter_value(self.EMAIL_INPUT, email)

    @allure.step("Вводим в поле Password '{password}'")
    def enter_password(self, password):
        self.enter_value(self.PASSWORD_INPUT, password)

    @allure.step("Отмечаем чек-бокс 'I have read and agree to the Privacy Policy'")
    def mark_policy_checkbox(self):
        self.click(self.POLICY_CHECKBOX)

    @allure.step("Нажимаем на кнопку 'Continue'")
    def submit_form(self):
        self.click(self.REGISTER_FORM_SUBMIT_BUTTON)

    @allure.step("Проверяем наличие ссылки 'Logout'")
    def logout_link_is_present(self):
        return self.get_element(self.LOGOUT_LINK)
