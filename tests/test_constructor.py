from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def test_move_to_buns_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.sauces_link))
    authorization.find_element(*TestLocators.sauces_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.buns_link))
    authorization.find_element(*TestLocators.buns_link).click()
    buns_class_constructor = authorization.find_element(*TestLocators.buns_class)
    current_class_constructor = authorization.find_element(*TestLocators.current_class)
    assert buns_class_constructor == current_class_constructor


def test_move_to_sauces_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.sauces_link))
    authorization.find_element(*TestLocators.sauces_link).click()
    sauces_class_constructor = authorization.find_element(*TestLocators.sauces_class)
    current_class_constructor = authorization.find_element(*TestLocators.current_class)
    assert sauces_class_constructor == current_class_constructor


def test_move_to_fillings_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.fillings_link))
    authorization.find_element(*TestLocators.fillings_link).click()
    fillings_class_constructor = authorization.find_element(*TestLocators.fillings_class)
    current_class_constructor = authorization.find_element(*TestLocators.current_class)
    assert fillings_class_constructor == current_class_constructor
