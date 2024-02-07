# Import necessary modules and classes
from Data import data
from Locators import locators
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from time import sleep


class TestForgotPassword:
    @pytest.fixture
    def setup(self):
        # Initialize the WebDriver using Firefox for test setup
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        # Quit the WebDriver to close the browser after the test
        self.driver.quit()

    def test_successful_password_reset_positive(self, setup):
        try:
            # When
            self.driver.get(data.WebData().url)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().invalid_password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

            # Navigate to the Forgot Password page
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()

            # Enter the username for password reset
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().resetpassword_username))).send_keys(
                data.WebData().reset_username)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().reset_button))).click()

            # Assert
            confirmation_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().reset_link_message)))
            assert confirmation_message.text == "A reset password link has been sent to you via email."

        except Exception as e:
            pytest.fail(f"Error in test_successful_password_reset_positive: {e}")

    def test_cancel_password_reset_negative(self, setup):
        try:
            self.driver.get(data.WebData().url)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().invalid_password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

            # Navigate to the Forgot Password page
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().cancel_button))).click()
            sleep(3)  # Introducing a sleep to allow for page redirection

            # Assert the URL after cancellation
            assert self.driver.current_url == data.WebData().url

        except Exception as e:
            pytest.fail(f"Error in test_cancel_password_reset_negative: {e}")

    def test_cancel_password_reset_negative2(self, setup):
        try:
            self.driver.get(data.WebData().url)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().invalid_password)
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()

            # Navigate to the Forgot Password page
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().cancel_button))).click()

            # Assert the URL after cancellation
            assert self.driver.current_url == data.WebData().dashboard_url

        except Exception as e:
            pytest.fail(f"Error in test_cancel_password_reset_negative2: {e}")

    def test_empty_username_field_negative(self, setup):
        try:
            self.driver.get(data.WebData().url)
            # Click on the "Forgot your password?" link
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()

            # Click on the Reset button without entering the username
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().reset_button))).click()

            # Verify the presence of error message
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().error))).text

            # Assert the error message
            assert "Required" in error_message

        except Exception as e:
            pytest.fail(f"Error in test_empty_username_field_negative: {e}")