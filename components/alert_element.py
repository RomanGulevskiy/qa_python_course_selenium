from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, browser):
        self.browser = browser

    def success_alert_is_present(self):
        return WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(self.SUCCESS_ALERT))