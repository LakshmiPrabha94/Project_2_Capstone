# Importing necessary modules and classes
from Locators import locators
import pytest
from Automation_Scripts.orange_menu_validation import Menu_validation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to set up the menu_list for testing
@pytest.fixture
def menu_list():
    # Creating an instance of Menu_validation class
    menu_list = Menu_validation()
    # Booting up the application
    menu_list.booting_function()
    # Performing login
    menu_list.login()
    WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin))).click()
    return menu_list


# Admin - Test cases for Admin menu validation
def test_admin_menu_label_present(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert "Admin" in admin_menu.text


def test_admin_menu_label_absent(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert "Admin" not in admin_menu.text


def test_admin_menu_displayed(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert admin_menu.is_displayed()


def test_admin_menu_not_displayed(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert not admin_menu.is_displayed()


def test_admin_menu_enabled(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert admin_menu.is_enabled()


def test_admin_menu_not_enabled(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert not admin_menu.is_enabled()


def test_admin_menu_selected(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert admin_menu.is_selected()


def test_admin_menu_not_selected(menu_list):
    admin_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin)))
    assert not admin_menu.is_selected()


# PIM - Test cases for PIM menu validation
def test_pim_menu_label_present(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert "PIM" in pim_menu.text


def test_pim_menu_label_absent(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert "PIM" not in pim_menu.text


def test_pim_menu_displayed(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert pim_menu.is_displayed()


def test_pim_menu_not_displayed(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert not pim_menu.is_displayed()


def test_pim_menu_enabled(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert pim_menu.is_enabled()


def test_pim_menu_not_enabled(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert not pim_menu.is_enabled()


def test_pim_menu_selected(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert pim_menu.is_selected()


def test_pim_menu_not_selected(menu_list):
    pim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().pim)))
    assert not pim_menu.is_selected()


# Leave - Test cases for Leave menu validation
def test_leave_menu_label_present(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert "Leave" in leave_menu.text


def test_leave_menu_label_absent(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert "Leave" not in leave_menu.text


def test_leave_menu_displayed(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert leave_menu.is_displayed()


def test_leave_menu_not_displayed(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert not leave_menu.is_displayed()


def test_leave_menu_enabled(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert leave_menu.is_enabled()


def test_leave_menu_not_enabled(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert not leave_menu.is_enabled()


def test_leave_menu_selected(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert leave_menu.is_selected()


def test_leave_menu_not_selected(menu_list):
    leave_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().leave)))
    assert not leave_menu.is_selected()


# Time - Test cases for Time menu validation
def test_time_menu_label_present(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert "Time" in time_menu.text


def test_time_menu_label_absent(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert "Time" not in time_menu.text


def test_time_menu_displayed(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert time_menu.is_displayed()


def test_time_menu_not_displayed(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert not time_menu.is_displayed()


def test_time_menu_enabled(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert time_menu.is_enabled()


def test_time_menu_not_enabled(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert not time_menu.is_enabled()


def test_time_menu_selected(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert time_menu.is_selected()


def test_time_menu_not_selected(menu_list):
    time_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().time)))
    assert not time_menu.is_selected()


# Recruitment - Test cases for Recruitment menu validation
def test_recruitment_menu_label_present(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert "Recruitment" in recruitment_menu.text


def test_recruitment_menu_label_absent(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert "Recruitment" not in recruitment_menu.text


def test_recruitment_menu_displayed(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert recruitment_menu.is_displayed()


def test_recruitment_menu_not_displayed(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert not recruitment_menu.is_displayed()


def test_recruitment_menu_enabled(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert recruitment_menu.is_enabled()


def test_recruitment_menu_not_enabled(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert not recruitment_menu.is_enabled()


def test_recruitment_menu_selected(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert recruitment_menu.is_selected()


def test_recruitment_menu_not_selected(menu_list):
    recruitment_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().recruitment)))
    assert not recruitment_menu.is_selected()


# My Info - Test cases for My Info menu validation
def test_myInfo_menu_label_present(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert "My Info" in myInfo_menu.text


def test_myInfo_menu_label_absent(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert "My Info" not in myInfo_menu.text


def test_myInfo_menu_displayed(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert myInfo_menu.is_displayed()


def test_myInfo_menu_not_displayed(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert not myInfo_menu.is_displayed()


def test_myInfo_menu_enabled(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert myInfo_menu.is_enabled()


def test_myInfo_menu_not_enabled(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert not myInfo_menu.is_enabled()


def test_myInfo_menu_selected(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert myInfo_menu.is_selected()


def test_myInfo_menu_not_selected(menu_list):
    myInfo_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().myInfo)))
    assert not myInfo_menu.is_selected()


# Performance - Test cases for Performance menu validation
def test_performance_menu_label_present(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert "Performance" in performance_menu.text


def test_performance_menu_label_absent(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert "Performance" not in performance_menu.text


def test_performance_menu_displayed(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert performance_menu.is_displayed()


def test_performance_menu_not_displayed(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert not performance_menu.is_displayed()


def test_performance_menu_enabled(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert performance_menu.is_enabled()


def test_performance_menu_not_enabled(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert not performance_menu.is_enabled()


def test_performance_menu_selected(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert performance_menu.is_selected()


def test_performance_menu_not_selected(menu_list):
    performance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().performance)))
    assert not performance_menu.is_selected()


# Dashboard - - Test cases for Dashboard menu validation
def test_dashboard_menu_label_present(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert "Dashboard" in dashboard_menu.text


def test_dashboard_menu_label_absent(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert "Dashboard" not in dashboard_menu.text


def test_dashboard_menu_displayed(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert dashboard_menu.is_displayed()


def test_dashboard_menu_not_displayed(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert not dashboard_menu.is_displayed()


def test_dashboard_menu_enabled(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert dashboard_menu.is_enabled()


def test_dashboard_menu_not_enabled(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert not dashboard_menu.is_enabled()


def test_dashboard_menu_selected(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert dashboard_menu.is_selected()


def test_dashboard_menu_not_selected(menu_list):
    dashboard_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().dashboard)))
    assert not dashboard_menu.is_selected()


# Directory - Test cases for Directory menu validation
def test_directory_menu_label_present(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert "Directory" in directory_menu.text


def test_directory_menu_label_absent(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert "Directory" not in directory_menu.text


def test_directory_menu_displayed(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert directory_menu.is_displayed()


def test_directory_menu_not_displayed(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert not directory_menu.is_displayed()


def test_directory_menu_enabled(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert directory_menu.is_enabled()


def test_directory_menu_not_enabled(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert not directory_menu.is_enabled()


def test_directory_menu_selected(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert directory_menu.is_selected()


def test_directory_menu_not_selected(menu_list):
    directory_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().directory)))
    assert not directory_menu.is_selected()


# Maintenance - Test cases for Maintenance menu validation
def test_maintenance_menu_label_present(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert "Maintenance" in maintenance_menu.text


def test_maintenance_menu_label_absent(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert "Maintenance" not in maintenance_menu.text


def test_maintenance_menu_displayed(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert maintenance_menu.is_displayed()


def test_maintenance_menu_not_displayed(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert not maintenance_menu.is_displayed()


def test_maintenance_menu_enabled(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert maintenance_menu.is_enabled()


def test_maintenance_menu_not_enabled(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert not maintenance_menu.is_enabled()


def test_maintenance_menu_selected(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert maintenance_menu.is_selected()


def test_maintenance_menu_not_selected(menu_list):
    maintenance_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().maintenance)))
    assert not maintenance_menu.is_selected()


# Claim - - Test cases for Claim menu validation
def test_claim_menu_label_present(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert "Claim" in claim_menu.text


def test_claim_menu_label_absent(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert "Claim" not in claim_menu.text


def test_claim_menu_displayed(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert claim_menu.is_displayed()


def test_claim_menu_not_displayed(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert not claim_menu.is_displayed()


def test_claim_menu_enabled(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert claim_menu.is_enabled()


def test_claim_menu_not_enabled(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert not claim_menu.is_enabled()


def test_claim_menu_selected(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert claim_menu.is_selected()


def test_claim_menu_not_selected(menu_list):
    claim_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().claim)))
    assert not claim_menu.is_selected()


# Buzz - Test cases for Buzz menu validation
def test_buzz_menu_label_present(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert "Buzz" in buzz_menu.text


def test_buzz_menu_label_absent(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert "Buzz" not in buzz_menu.text


def test_buzz_menu_displayed(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert buzz_menu.is_displayed()


def test_buzz_menu_not_displayed(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert not buzz_menu.is_displayed()


def test_buzz_menu_enabled(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert buzz_menu.is_enabled()


def test_buzz_menu_not_enabled(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert not buzz_menu.is_enabled()


def test_buzz_menu_selected(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert buzz_menu.is_selected()


def test_buzz_menu_not_selected(menu_list):
    buzz_menu = WebDriverWait(menu_list.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, locators.WebLocators().buzz)))
    assert not buzz_menu.is_selected()