import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    name = 'Andrew'
    random_number = random.randint(1000, 9999)
    email = "Fursov_08_" + str(random_number) + "@ya.ru"
    password = 'qwe123'

    def test_registration(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.BUTTON_GO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_REGISTER)))

        driver.find_element(*locator.NAME_FIELD).send_keys(TestRegistration.name)
        driver.find_element(*locator.MAIL_FIELD).send_keys(TestRegistration.email)
        driver.find_element(*locator.PASSWORD_FIELD).send_keys(TestRegistration.password)
        driver.find_element(*locator.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        reg = driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).text
        assert reg == 'Войти'

    def test_eroor_password(self,driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.BUTTON_GO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_REGISTER)))

        driver.find_element(*locator.NAME_FIELD).send_keys(TestRegistration.name)
        driver.find_element(*locator.MAIL_FIELD).send_keys(TestRegistration.email)
        driver.find_element(*locator.PASSWORD_FIELD).send_keys('123qw')
        driver.find_element(*locator.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator.PASSWORD_ERROR_NOTIFICATION))

        error = driver.find_element(*locator.PASSWORD_ERROR_NOTIFICATION).text
        assert error == 'Некорректный пароль'
