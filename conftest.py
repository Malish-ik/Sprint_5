import random

import pytest
import data
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(data.main_page)
    #return driver
    yield driver
    driver.quit()


@pytest.fixture
def new_user():
    user_name = f'inna_kalacheva_9_{random.randint(100, 998)}'
    email = f'{user_name}@yandex.ru'
    user = {"user_name": user_name,
            "email": email,
            "password": "8765432"}
    return user


@pytest.fixture
def authorization(driver):
    driver.find_element(*TestLocators.button_enter_page_main).click()
    driver.find_element(*TestLocators.authorization_email).send_keys(data.email)
    driver.find_element(*TestLocators.authorization_password).send_keys(data.password_valid)
    driver.find_element(*TestLocators.button_authorization).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.personal_account_link))
    driver.find_element(*TestLocators.personal_account_link).click()
    return driver
