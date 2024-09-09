import pytest
import logging
import datetime
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", default="chrome", choices=["chrome", "firefox"]),
    parser.addoption("--headless", "-H", action="store_true"),
    parser.addoption("--url", "-U", default="http://opencart:8080")
    parser.addoption("--executor", "-E"),
    parser.addoption("--log_level", "-L", default="INFO")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    base_url = request.config.getoption("--url")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    test_name = request.node.name

    logger = logging.getLogger(test_name)
    os.makedirs("log", exist_ok=True)
    file_handler = logging.FileHandler(f"log/{test_name}.log", encoding='utf-8')
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)

    logger.info("===> Test '%s' started at %s" % (test_name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless_mode:
            options.add_argument("headless=new")
        if not executor:
            driver = webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        if not executor:
            driver = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    if executor:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser_name,
            "browserVersion": '126.0',
            "selenoid:options": {
                "enableVNC": True,
                "name": request.node.name,
                "screenResolution": "1920x1080",
                "enableVideo": False,
                "enableLog": False,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            },
            "acceptInsecureCerts": True,
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    driver.maximize_window()
    driver.url = base_url
    driver.logger = logger

    def fin():
        driver.quit()
        logger.info("===> Test '%s' finished at %s" % (test_name, datetime.datetime.now()))

    request.addfinalizer(fin)

    return driver
