from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
from Locators import locators


class Header_validation:
    # Initialize the WebDriver using Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def booting_function(self):
        try:
            # Maximize the browser window and open the specified URL
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            print("Browser started successfully.")
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        # Quit the WebDriver to close the browser
        self.driver.quit()

    def login(self):
        try:
            # Wait for the username field to be visible and enter the username
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            # Enter the password
            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)

            # click on the login button
            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def header_validation(self):
        # Click on the Admin menu option
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin_locator))).click()

        # List of header options on the Admin page
        header_options = ["User Management", "Job", "Organisation", "Qualification", "Nationalities",
                          "Corporate Branding", "Configuration"]

        # Verify header options on the Admin page
        for index, option in enumerate(header_options, start=1):
            locator = f"//header/div[2]/nav/ul/li[{index}]"
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
                print(f"{option} is displayed.")
            except:
                print(f"{option} is NOT displayed.")


# Main block to execute the script
if __name__ == '__main__':
    # Create an instance of the HeaderValidation class
    header_list = Header_validation()
    # Check if the browser is successfully launched and login is successful
    if header_list.booting_function() and header_list.login():
        # Perform header validation
        header_list.header_validation()
        header_list.shutdown()


