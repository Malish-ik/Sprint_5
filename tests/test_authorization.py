import data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def test_auth_main_page(driver):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.authorization_email).send_keys(data.email)
    driver.find_element(*TestLocators.authorization_password).send_keys(data.password_valid)
    driver.find_element(*TestLocators.button_authorization).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
    assert driver.find_element(*TestLocators.button_order).is_displayed()


def test_auth_personal_account(driver):
    driver.find_element(*TestLocators.personal_account_link).click()
    driver.find_element(*TestLocators.authorization_email).send_keys(data.email)
    driver.find_element(*TestLocators.authorization_password).send_keys(data.password_valid)
    driver.find_element(*TestLocators.button_authorization).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
    assert driver.find_element(*TestLocators.button_order).is_displayed()


def test_auth_registration_link(driver):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.registration_link).click()
    driver.find_element(*TestLocators.authorization_link).click()
    driver.find_element(*TestLocators.authorization_email).send_keys(data.email)
    driver.find_element(*TestLocators.authorization_password).send_keys(data.password_valid)
    driver.find_element(*TestLocators.button_authorization).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
    assert driver.find_element(*TestLocators.button_order).is_displayed()


def test_auth_forgot_password_link(driver):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.forgot_password_link).click()
    driver.find_element(*TestLocators.authorization_link).click()
    driver.find_element(*TestLocators.authorization_email).send_keys(data.email)
    driver.find_element(*TestLocators.authorization_password).send_keys(data.password_valid)
    driver.find_element(*TestLocators.button_authorization).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.button_order))
    assert driver.find_element(*TestLocators.button_order).is_displayed()
