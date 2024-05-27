import allure
import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 3)
        self.logger = browser.logger

    def get_element(self, locator: tuple):
        try:
            self.logger.info(f"Check if '{locator}' element is present")
            return self.wait.until(EC.visibility_of_element_located(locator))
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    def get_elements(self, locator: tuple):
        try:
            self.logger.info(f"Check if '{locator}' elements are present")
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    def click(self, locator: tuple):
        try:
            self.logger.info(f"Click '{locator}' element")
            ActionChains(self.browser).move_to_element(self.get_element(locator)).click().perform()
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError

    def enter_value(self, locator: tuple, text: str):
        try:
            self.logger.info(f"Enter '{text}' into {locator}")
            input_field = self.get_element(locator)
            input_field.click()
            input_field.clear()
            input_field.send_keys(text)
        except selenium.common.exceptions.TimeoutException:
            allure.attach(body=self.browser.get_screenshot_as_png(),
                          name="failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError
