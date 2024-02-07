"""
TC_PIM_03 - Menu Validation
Test Objective: Menu validation on the Admin page
Expected Results: The user should be able to see the Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, and Buzz Menu options on the Admin page.
"""
# Importing necessary modules and classes
from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Menu_validation:
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

    def menu_validation(self):

        # Click on the Admin menu option
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin_locator))).click()

        # List of header options in the Admin page
        menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                        "Directory", "Maintenance", "Claim", "Buzz"]

        # Verify menu options on the Admin page
        for option in menu_options:
            locator = f"//li/a/span[text()='{option}']"
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
                print(f"{option} is displayed.")
            except:
                print(f"{option} is NOT displayed.")


# Main block to execute the script
if __name__ == '__main__':
    # Create an instance of the MenuValidation class
    menu_list = Menu_validation()
    # Check if the browser is successfully launched and login is successful
    if menu_list.booting_function() and menu_list.login():
        # Perform menu validation
        menu_list.menu_validation()


