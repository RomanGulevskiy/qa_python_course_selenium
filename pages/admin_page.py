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
        self.browser.get(self.browser.url + self.PATH)

    def enter_username(self, username):
        self.enter_value(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_value(self.PASSWORD_INPUT, password)

    def submit_form(self):
        self.click(self.LOGIN_FORM_SUBMIT_BUTTON)

    def logout_link_is_present(self):
        return self.get_element(self.LOGOUT_LINK)

    def logout(self):
        self.click(self.LOGOUT_LINK)

    def login_button_is_present(self):
        return self.get_element(self.LOGIN_FORM_SUBMIT_BUTTON)

    def navigate_to_catalog_products(self):
        self.click(self.CATALOG_MENU_LINK)
        self.click(self.CATALOG_PRODUCTS_MENU_LINK)