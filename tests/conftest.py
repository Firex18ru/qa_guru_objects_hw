import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1680
    browser.config.window_width = 1050
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    yield

    browser.quit()
