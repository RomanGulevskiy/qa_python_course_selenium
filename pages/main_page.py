import time
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    FEATURED_PRODUCT_NAME = (By.CSS_SELECTOR, '#content > div.row .product-thumb h4 a')
    FEATURED_PRODUCT_CART_BUTTON = (By.CSS_SELECTOR, 'div.button-group > button:nth-child(1)')

    def open(self):
        with allure.step(f"Открываем страницу {self.browser.url}"):
            self.browser.get(self.browser.url)

    @allure.step("Получаем наименование товара (по индексу)")
    def get_featured_product_name(self, index=0):
        return self.get_elements(self.FEATURED_PRODUCT_NAME)[index].text

    @allure.step("Добавляем товар в корзину (по индексу)")
    def add_featured_product_to_cart(self, index=0):
        el = self.get_elements(self.FEATURED_PRODUCT_CART_BUTTON)[index]
        time.sleep(1)
        ActionChains(self.browser).move_to_element(el).click().perform()
