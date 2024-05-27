import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CurrencySwitcher(BasePage):
    CURRENCY_MENU_BUTTON = (By.XPATH, '//*[@id="form-currency"]/div')
    CURRENT_CURRENCY_TEXT = (By.XPATH, '//*[@id="form-currency"]/div/a/strong')
    EURO_LINK = (By.LINK_TEXT, "€ Euro")
    USD_LINK = (By.LINK_TEXT, "$ US Dollar")
    GBP_LINK = (By.LINK_TEXT, "£ Pound Sterling")

    @allure.step("Переключаем валюту на EUR")
    def switch_to_euro(self):
        self.click(self.CURRENCY_MENU_BUTTON)
        self.click(self.EURO_LINK)

    @allure.step("Переключаем валюту на USD")
    def switch_to_usd(self):
        self.click(self.CURRENCY_MENU_BUTTON)
        self.click(self.USD_LINK)

    @allure.step("Переключаем валюту на GBP")
    def switch_to_gbp(self):
        self.click(self.CURRENCY_MENU_BUTTON)
        self.click(self.GBP_LINK)

    @property
    @allure.step("Получаем название текущей валюты")
    def current_currency(self):
        return self.get_element(self.CURRENT_CURRENCY_TEXT).text
