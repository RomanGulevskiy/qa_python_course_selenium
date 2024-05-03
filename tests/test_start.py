from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_is("Your Store"), "За время ожидания не найден корректный title страницы")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".carousel")))
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="content"]/h3'), "Featured"))


def test_admin_page(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_is("Administration"), "За время ожидания не найден корректный title страницы")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "OpenCart")))


def test_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_is("Register Account"), "За время ожидания не найден корректный title страницы")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-register")))
    wait.until(EC.visibility_of_element_located((By.NAME, "firstname")))
    wait.until(EC.visibility_of_element_located((By.NAME, "lastname")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-check")))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-register"]/div/button')))


def test_catalog_page(browser):
    browser.get(browser.url + "/index.php?route=product/category&language=en-gb&path=25_28")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-category")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#display-control")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-list")))


def test_product_page(browser):
    browser.get(browser.url + "/index.php?route=product/product&language=en-gb&product_id=42&path=25_28")
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-info")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".rating")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Description")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Specification")))
    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Reviews")))


def test_add_to_cart(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    # Получаем название товара
    product = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="product-thumb"]')))[1]
    product_name = product.find_element(By.XPATH, 'div[2]/div/h4/a').text
    # Добавляем товар в корзину
    product.find_element(By.XPATH, 'div[2]/form/div/button[1]').click()
    # Проверяем сообщение об успехе
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
    # Ждем обновление корзины
    wait.until(EC.staleness_of(browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')))
    # Открываем корзину
    cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-cart")))
    cart.find_element(By.XPATH, 'div/button').click()
    # Проверяем наличие товара в корзине
    cart.find_element(By.LINK_TEXT, product_name)


def test_main_change_currency(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 2)
    # Получаем стоимость товара в старой валюте
    old_price = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    # Изменяем валюту
    browser.find_element(By.CSS_SELECTOR, "#form-currency").click()
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Euro"))).click()
    # Получаем стоимость товара в новой валюте
    new_price = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    assert old_price != new_price


def test_catalog_change_currency(browser):
    browser.get(browser.url + "/index.php?route=product/category&language=en-gb&path=25_28")
    wait = WebDriverWait(browser, 2)
    # Получаем стоимость товара в старой валюте
    old_price = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    # Изменяем валюту
    browser.find_element(By.CSS_SELECTOR, "#form-currency").click()
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Euro"))).click()
    # Получаем стоимость товара в новой валюте
    new_price = browser.find_element(By.CSS_SELECTOR, ".price-new").text
    assert old_price != new_price


def test_login(browser):
    browser.get(browser.url + "/administration")
    # Выполняем логин
    browser.find_element(By.NAME, "username").send_keys("admin")
    browser.find_element(By.NAME, "password").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    # Выполняем логаут
    logout_btn = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-logout")))
    logout_btn.click()

