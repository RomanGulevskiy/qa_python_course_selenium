import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    FEATURED_PRODUCT_NAME = (By.CSS_SELECTOR, '#content > div.row .product-thumb h4 a')
    FEATURED_PRODUCT_CART_BUTTON = (By.CSS_SELECTOR, 'div.button-group > button:nth-child(1)')

    def open(self):
        self.browser.get(self.browser.url)

    def get_featured_product_name(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAME)[index].text

    def add_featured_product_to_cart(self, index=0):
        el = self.get_elements(self.FEATURED_PRODUCT_CART_BUTTON)[index]
        time.sleep(1)
        ActionChains(self.browser).move_to_element(el).click().perform()
