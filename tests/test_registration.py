from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


def test_registration_successfully(driver, new_user):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.registration_link).click()
    driver.find_element(*TestLocators.registration_name).send_keys(new_user['user_name'])
    driver.find_element(*TestLocators.registration_email).send_keys(new_user['email'])
    driver.find_element(*TestLocators.registration_password).send_keys(new_user['password'])
    driver.find_element(*TestLocators.button_registration).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(TestLocators.button_authorization))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()


def test_registration_invalid_password(driver, new_user):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.registration_link).click()
    driver.find_element(*TestLocators.registration_name).send_keys(new_user['user_name'])
    driver.find_element(*TestLocators.registration_email).send_keys(new_user['email'])
    driver.find_element(*TestLocators.registration_password).send_keys(new_user['password'][:2])
    driver.find_element(*TestLocators.button_registration).click()
    assert driver.find_element(*TestLocators.incorrect_password_error).text == "Некорректный пароль"
    driver.quit()
