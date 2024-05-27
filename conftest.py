import pytest
import logging
import datetime
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome", choices=["chrome", "ff"]),
    parser.addoption("--headless", "-H", action="store_true"),
    parser.addoption("--url", "-U", default="http://opencart.local"),
    parser.addoption("--log_level", "-L", default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    test_name = request.node.name

    logger = logging.getLogger(test_name)
    os.makedirs("log", exist_ok=True)
    file_handler = logging.FileHandler(f"log/{test_name}.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    logger.info("===> Test '%s' started at %s" % (test_name, datetime.datetime.now()))

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
    driver.url = base_url
    driver.logger = logger

    def fin():
        driver.quit()
        logger.info("===> Test '%s' finished at %s" % (test_name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver
