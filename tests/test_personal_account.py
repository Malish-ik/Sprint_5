from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def test_move_to_personal_account(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.button_profile))
    assert authorization.find_element(*TestLocators.button_profile).text == "Профиль"
    authorization.quit()


def test_move_to_constructor(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.header_burger))
    assert authorization.find_element(*TestLocators.header_burger).text == "Соберите бургер"
    authorization.quit()


def test_move_to_logo(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.logo_stellar_burgers))
    authorization.find_element(*TestLocators.logo_stellar_burgers).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.header_burger))
    assert authorization.find_element(*TestLocators.header_burger).text == "Соберите бургер"
    authorization.quit()


def test_exit_personal_account(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.button_exit_personal_account))
    authorization.find_element(*TestLocators.button_exit_personal_account).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.header_enter))
    assert authorization.find_element(*TestLocators.header_enter).text == "Вход"
    authorization.quit()
