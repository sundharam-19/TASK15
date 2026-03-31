import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    # The URL has a typo in the prompt. The correct URL for OrangeHRM demo is:
    # https://orangehrmlive.com
    driver.get("https://orangehrmlive.com")
    yield driver
    # Close the browser after the test
    driver.quit()