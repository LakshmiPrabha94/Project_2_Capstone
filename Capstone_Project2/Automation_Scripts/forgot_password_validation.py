# # Import necessary modules and classes
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
from Locators import locators


class PasswordResetValidation:
    # Initialize the WebDriver using Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def booting_function(self):
        try:
            # Maximize the browser window
            self.driver.maximize_window()

            # Open the specified URL
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        # Quit the WebDriver to close the browser
        self.driver.quit()

    def forgot_password(self):
        try:
            # Find the username field and enter the username
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            # Click on the "Forgot your password?" link
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()

            # Enter the username for which the password needs to be reset
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().resetpassword_username))).send_keys(
                data.WebData().reset_username)
            print("Entering username: ", data.WebData().reset_username)

            # Click on the Reset button
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().reset_button))).click()
            print("Password reset initiated successfully.")

        except Exception as e:
            print(f"Error during password reset: {e}")

        # Main block to execute the script


if __name__ == "__main__":
    # Create an instance of the PasswordResetValidation class
    password_reset_validator = PasswordResetValidation()

    # Check if the browser is successfully launched
    if password_reset_validator.booting_function():
        # Trigger the password reset function
        password_reset_validator.forgot_password()
