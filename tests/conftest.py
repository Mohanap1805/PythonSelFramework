import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store",default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(4)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
