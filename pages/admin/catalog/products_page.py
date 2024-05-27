import allure
import random
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ProductsPage(BasePage):
    ADD_NEW_PRODUCT_LINK = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')
    PRODUCT_CHECKBOXES = (By.CSS_SELECTOR, ".form-check-input")

    @allure.step("Нажимаем на ссылку 'Add New'")
    def add_new_product_link_click(self):
        self.click(self.ADD_NEW_PRODUCT_LINK)

    @allure.step("Нажимаем на кнопку 'Delete'")
    def delete_product_button_submit(self):
        self.click(self.DELETE_PRODUCT_BUTTON)

    @allure.step("Отмечаем случайный товар в списке")
    def select_random_product(self):
        products_list = self.get_elements(self.PRODUCT_CHECKBOXES)
        random_choice = random.randint(1, len(products_list) - 1)
        el = self.get_elements(self.PRODUCT_CHECKBOXES)[random_choice]
        ActionChains(self.browser).move_to_element(el).click().perform()

    @allure.step("Подтверждаем удаление товара в alert-е")
    def delete_product_alert_accept(self):
        alert = self.browser.switch_to.alert
        alert.accept()