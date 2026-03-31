from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.login_button_locator = (By.XPATH, "//button[normalize-space()='Login']")
        self.dashboard_header_locator = (By.XPATH, "//h6[normalize-space()='Dashboard']")
        self.invalid_credentials_locator = (By.XPATH, "//p[normalize-space()='Invalid credentials']")
        self.wait = WebDriverWait(driver, 10) # Explicit wait with 10 seconds timeout

    def login(self, username, password):
        # Use explicit wait for elements to be present and interactive
        username_field = self.wait.until(EC.element_to_be_clickable(self.username_locator))
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.wait.until(EC.element_to_be_clickable(self.password_locator))
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button_locator))
        login_button.click()

    def is_login_successful(self):
        try:
            # Wait for the dashboard header to be visible (success indicator)
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header_locator))
            return True
        except:
            return False

    def get_error_message(self):
        try:
            # Wait for the error message to be visible
            error_message = self.wait.until(EC.visibility_of_element_located(self.invalid_credentials_locator))
            return error_message.text
        except:
            return None
