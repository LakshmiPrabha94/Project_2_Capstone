"""

TC_PIM_02 - Header Validation Test Script

Description: This automation script validates the headers displayed on the Admin page of the OrangeHRM portal.
Steps:
Navigate to the Admin page of the OrangeHRM portal.
Verify the presence of the following header options: User Management, Job, Organization, Qualification, Nationalities, Corporate Banking, and Configuration.
Expected Outcome: The script expects the user to be able to see all the specified header options displayed on the Admin page, ensuring that the page layout and navigation are as expected

"""
# Importing necessary modules and classes
import pytest
from Automation_Scripts.orange_header_validation import Header_validation
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators import locators

@pytest.fixture
def header_validator():
    header_validator = Header_validation()
    header_validator.booting_function()
    header_validator.login()
    WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin))).click()
    return header_validator

# User Management
def test_user_management_label_present(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert "User Management" in user_management_option.text
def test_user_management_label_absent(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert "User Management" not in user_management_option.text
def test_user_management_displayed(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert user_management_option.is_displayed()
def test_user_management_not_displayed(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert not user_management_option.is_displayed()
def test_user_management_enabled(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert user_management_option.is_enabled()
def test_user_management_not_enabled(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert not user_management_option.is_enabled()
def test_user_management_selected(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert user_management_option.is_selected() == "True"
def test_user_management_not_selected(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    assert not user_management_option.is_selected()
#Job
def test_job_label_present(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert "Job" in job_option.text
def test_job_label_absent(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert "Job" not in job_option.text
def test_job_displayed(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert job_option.is_displayed()
def test_job_not_displayed(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert not job_option.is_displayed()
def test_job_enabled(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert job_option.is_enabled()
def test_job_not_enabled(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert not job_option.is_enabled()
def test_job_selected(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert job_option.is_selected()
def test_job_not_selected(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    assert not job_option.is_selected()

# Organization
def test_organisation_label_present(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert "Organization" in organisation_option.text
def test_organisation_label_absent(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert "Organization" not in organisation_option.text
def test_organisation_displayed(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert organisation_option.is_displayed()
def test_organisation_not_displayed(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert not organisation_option.is_displayed()
def test_organisation_enabled(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert organisation_option.is_enabled()
def test_organisation_not_enabled(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert not organisation_option.is_enabled()
def test_organisation_selected(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert organisation_option.is_selected()
def test_organisation_not_selected(header_validator):
    organisation_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    assert not organisation_option.is_selected()

#Qualification
def test_qualification_label_present(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert "Qualification" in qualification_option.text
def test_qualification_label_absent(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert "Qualification" not in qualification_option.text
def test_qualification_displayed(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert qualification_option.is_displayed()
def test_qualification_not_displayed(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert not qualification_option.is_displayed()
def test_qualification_enabled(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert qualification_option.is_enabled()
def test_qualification_not_enabled(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert not qualification_option.is_enabled()
def test_qualification_selected(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert qualification_option.is_selected()
def test_qualification_not_selected(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    assert not qualification_option.is_selected()

# Nationality
def test_nationality_label_present(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert "Nationalities" in nationality_option.text
def test_nationality_label_absent(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert "Nationalities" not in nationality_option.text
def test_nationality_displayed(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert nationality_option.is_displayed()
def test_nationality_not_displayed(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert not nationality_option.is_displayed()
def test_nationality_enabled(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert nationality_option.is_enabled()
def test_nationality_not_enabled(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert not nationality_option.is_enabled()
def test_nationality_selected(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert nationality_option.is_selected()
def test_nationality_not_selected(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    assert not nationality_option.is_selected()

# Corporate Branding
def test_corporate_branding_label_present(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert "Corporate Branding" in corporate_branding_option.text
def test_corporate_branding_label_absent(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert "Corporate Branding" not in corporate_branding_option.text
def test_corporate_branding_displayed(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert corporate_branding_option.is_displayed()
def test_corporate_branding_not_displayed(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert not corporate_branding_option.is_displayed()
def test_corporate_branding_enabled(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert corporate_branding_option.is_enabled()
def test_corporate_branding_not_enabled(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert not corporate_branding_option.is_enabled()
def test_corporate_branding_selected(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert corporate_branding_option.is_selected()
def test_corporate_branding_not_selected(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    assert not corporate_branding_option.is_selected()

# Configuration
def test_configuration_label_present(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert "Configuration" in configuration_option.text
def test_configuration_label_absent(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert "Configuration" not in configuration_option.text
def test_configuration_displayed(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert configuration_option.is_displayed()
def test_configuration_not_displayed(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert not configuration_option.is_displayed()
def test_configuration_enabled(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert configuration_option.is_enabled()
def test_configuration_not_enabled(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert not configuration_option.is_enabled()
def test_configuration_selected(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert configuration_option.is_selected()
def test_configuration_not_selected(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    assert not configuration_option.is_selected()

# Header clickability
def test_user_management_option_click(header_validator):
    user_management_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().userManagement)))
    user_management_option.click()
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in header_validator.driver.current_url

def test_job_option_click(header_validator):
    job_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().job)))
    job_option.click()
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in header_validator.driver.current_url

def test_organization_option_click(header_validator):
    organization_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().organisation)))
    organization_option.click()
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in header_validator.driver.current_url

def test_qualification_option_click(header_validator):
    qualification_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().qualification)))
    qualification_option.click()
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in header_validator.driver.current_url

def test_nationality_option_click(header_validator):
    nationality_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().nationalities)))
    nationality_option.click()
    sleep(2)
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality" in header_validator.driver.current_url

def test_corporate_branding_option_click(header_validator):
    corporate_branding_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().corporateBranding)))
    corporate_branding_option.click()
    sleep(2)
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/addTheme" in header_validator.driver.current_url

def test_configuration_option_click(header_validator):
    configuration_option = WebDriverWait(header_validator.driver, 20).until(EC.visibility_of_element_located((By.XPATH, locators.WebLocators().configuration)))
    configuration_option.click()
    assert "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers" in header_validator.driver.current_url




