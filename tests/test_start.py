from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.admin_page import AdminPage
from pages.admin.catalog.products_page import ProductsPage
from pages.admin.catalog.add_new_product_page import AddNewProductPage
from components.currency_switcher import CurrencySwitcher
from components.alert_element import AlertElement


def test_admin_login(browser):
    admin_page = AdminPage(browser)

    admin_page.open()
    admin_page.enter_username("admin")
    admin_page.enter_password("admin")
    admin_page.submit_form()
    assert admin_page.logout_link_is_present()

    admin_page.logout()
    assert admin_page.login_button_is_present()


def test_register_user(browser):
    register_page = RegisterPage(browser)

    register_page.open()
    register_page.enter_firstname("Name")
    register_page.enter_lastname("Lastname")
    register_page.enter_email("mail@mail.mail")
    register_page.enter_password("test")
    register_page.mark_policy_checkbox()
    register_page.submit_form()
    assert register_page.logout_link_is_present()


def test_change_currency(browser):
    main_page = MainPage(browser)
    currency_element = CurrencySwitcher(browser)

    main_page.open()

    currency_element.switch_to_usd()
    assert currency_element.current_currency == "$"

    currency_element.switch_to_euro()
    assert currency_element.current_currency == "€"

    currency_element.switch_to_gbp()
    assert currency_element.current_currency == "£"


def test_add_new_product(browser):
    admin_page = AdminPage(browser)
    products_page = ProductsPage(browser)
    add_new_product_page = AddNewProductPage(browser)
    alert_element = AlertElement(browser)

    admin_page.open()
    admin_page.enter_username("admin")
    admin_page.enter_password("admin")
    admin_page.submit_form()
    admin_page.navigate_to_catalog_products()

    products_page.add_new_product_link_click()

    add_new_product_page.enter_product_name("test product")
    add_new_product_page.enter_description("test description")
    add_new_product_page.enter_meta_tag_title("test meta tag title")
    add_new_product_page.open_data_tab()
    add_new_product_page.enter_model("test model")
    add_new_product_page.open_seo_tab()
    add_new_product_page.enter_seo_keywords("seo-keywords")
    add_new_product_page.submit_form()

    assert alert_element.success_alert_is_present()


def test_delete_random_product(browser):
    admin_page = AdminPage(browser)
    products_page = ProductsPage(browser)
    alert_element = AlertElement(browser)

    admin_page.open()
    admin_page.enter_username("admin")
    admin_page.enter_password("admin")
    admin_page.submit_form()
    admin_page.navigate_to_catalog_products()

    products_page.select_random_product()
    products_page.delete_product_button_submit()
    products_page.delete_product_alert_accept()

    assert alert_element.success_alert_is_present()
