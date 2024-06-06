from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


def test_move_to_buns_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.bun_name))
    assert authorization.find_element(*TestLocators.bun_name).text == 'Флюоресцентная булка R2-D3'
    authorization.quit()


def test_move_to_sauces_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.sauces_link))
    authorization.find_element(*TestLocators.sauces_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.sauce_name))
    assert authorization.find_element(*TestLocators.sauce_name).text == 'Соус Spicy-X'
    authorization.quit()


def test_move_to_fillings_section(authorization):
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.constructor_link))
    authorization.find_element(*TestLocators.constructor_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.fillings_link))
    authorization.find_element(*TestLocators.fillings_link).click()
    WebDriverWait(authorization, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.filling_name))
    assert authorization.find_element(*TestLocators.filling_name).text == 'Мясо бессмертных моллюсков Protostomia'
    authorization.quit()
