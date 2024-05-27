import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddNewProductPage(BasePage):
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button')
    # GENERAL TAB
    GENERAL_TAB_LINK = (By.LINK_TEXT, "General")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    META_TAG_DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "#input-meta-description-1")
    META_TAG_KEYWORDS_TEXTAREA = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    PRODUCT_TAGS_INPUT = (By.CSS_SELECTOR, "#input-tag-1")
    # DATA TAB
    DATA_TAB_LINK = (By.LINK_TEXT, "Data")
    MODEL_INPUT = (By.CSS_SELECTOR, "#input-model")
    # SEO TAB
    SEO_TAB_LINK = (By.LINK_TEXT, "SEO")
    SEO_KEYWORDS_INPUT = (By.CSS_SELECTOR, "#input-keyword-0-1")

    @allure.step("Открываем вкладку General")
    def open_general_tab(self):
        self.click(self.GENERAL_TAB_LINK)

    @allure.step("Открываем вкладку Data")
    def open_data_tab(self):
        self.click(self.DATA_TAB_LINK)

    @allure.step("Открываем вкладку SEO")
    def open_seo_tab(self):
        self.click(self.SEO_TAB_LINK)

    @allure.step("Вводим в поле Product name '{name}'")
    def enter_product_name(self, name):
        self.enter_value(self.PRODUCT_NAME_INPUT, name)

    @allure.step("Вводим в поле Description '{description}'")
    def enter_description(self, description):
        frames = self.get_elements((By.CSS_SELECTOR, "iframe"))
        self.browser.switch_to.frame(frames[0])
        description_input = self.get_element((By.XPATH, "/html/body/p"))
        description_input.send_keys(description)
        self.browser.switch_to.default_content()

    @allure.step("Вводим в поле Meta tag title '{title}'")
    def enter_meta_tag_title(self, title):
        self.enter_value(self.META_TAG_TITLE_INPUT, title)

    @allure.step("Вводим в поле Model '{model}'")
    def enter_model(self, model):
        self.enter_value(self.MODEL_INPUT, model)

    @allure.step("Вводим в поле Keyword '{keywords}'")
    def enter_seo_keywords(self, keywords):
        self.enter_value(self.SEO_KEYWORDS_INPUT, keywords)

    @allure.step("Нажимаем на кнопку 'Save'")
    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)