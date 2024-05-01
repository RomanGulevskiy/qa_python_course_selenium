import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome", choices=["chrome", "ff"]),
    parser.addoption("--headless", "-H", action="store_true"),
    parser.addoption("--url", "-U", default="http://opencart.local")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")

    if browser_name == "chrome":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("headless=new")
        driver = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    driver.maximize_window()
    request.addfinalizer(driver.quit)
    driver.url = base_url
    return driver
