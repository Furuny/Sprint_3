import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransition:
    email = "Fursov_08@ya.ru"
    password = 'йцу123йцу'
    def test_go_to_personal_account(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestTransition.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestTransition.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER)))

        driver.find_element(*locator.PERSONAL_AREA).click()

        lk = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ORDER_HISTORY))).text
        assert lk == 'История заказов'

    def test_transition_to_constructor_and_logo(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestTransition.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestTransition.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER)))

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ORDER_HISTORY)))

        driver.find_element(*locator.BURGER_CONSTRUCTOR).click()

        constructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert constructor == 'Оформить заказ'

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ORDER_HISTORY)))
        driver.find_element(*locator.LOGO).click()

        logo = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert logo == 'Оформить заказ'


    def test_exit_from_account(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestTransition.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestTransition.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER)))

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ORDER_HISTORY)))

        driver.find_element(*locator.LOGOUT_BUTTON).click()
        exit = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE))).text
        assert exit == 'Войти'

    def test_constructor_journey_to_sections(self, driver):
        element_bun = driver.find_element(*locator.BUN)
        driver.execute_script("arguments[0].scrollIntoView();", element_bun)
        assert WebDriverWait(driver, 7).until(expected_conditions.visibility_of_element_located((locator.BUN_CHOSEN)))

        element_sauce = driver.find_element(*locator.SAUCE)
        driver.execute_script("arguments[0].scrollIntoView();", element_sauce)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locator.SAUCE_CHOSEN)))

        element_filling = driver.find_element(*locator.FILLING_CHEEZE)
        driver.execute_script("arguments[0].scrollIntoView();", element_filling)
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locator.FILLING_CHOSEN)))
