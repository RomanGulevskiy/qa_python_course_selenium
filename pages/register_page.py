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
        self.browser.get(self.browser.url + self.PATH)

    def enter_firstname(self, firstname):
        self.enter_value(self.FIRSTNAME_INPUT, firstname)

    def enter_lastname(self, lastname):
        self.enter_value(self.LASTNAME_INPUT, lastname)

    def enter_email(self, email):
        self.enter_value(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_value(self.PASSWORD_INPUT, password)

    def mark_policy_checkbox(self):
        self.click(self.POLICY_CHECKBOX)

    def submit_form(self):
        self.click(self.REGISTER_FORM_SUBMIT_BUTTON)

    def logout_link_is_present(self):
        return self.get_element(self.LOGOUT_LINK)

