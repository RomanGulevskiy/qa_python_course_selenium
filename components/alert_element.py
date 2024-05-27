import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AlertElement(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    @allure.step("Проверяем наличие уведомления об успехе")
    def success_alert_is_present(self):
        return self.get_element(self.SUCCESS_ALERT)
