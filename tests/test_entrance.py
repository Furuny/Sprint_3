import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEntrance():
    email = "Fursov_08@ya.ru"
    password = 'йцу123йцу'

    def test_entrance_from_main(self, driver,):

        driver.find_element(*locator.LOG_IN_ACCOUNT_FROM_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestEntrance.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestEntrance.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        log_s_glavn = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert log_s_glavn == 'Оформить заказ', 'Не найдена кнопка Оформить заказ. логирование с главной не произошло'
        print('Успешное логирование с главной')

    def test_input_through_lk(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestEntrance.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestEntrance.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()


        log_cherez_lk = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert log_cherez_lk == 'Оформить заказ', "Не найдена кнопка Оформить заказ. Логирование через личный кабинет не произошло"
        print('Успешное логирование через личный кабинет')

    def test_login_through_registration(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.BUTTON_GO_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.EXIT_FROM_REGISTRATION)))

        driver.find_element(*locator.EXIT_FROM_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestEntrance.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestEntrance.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        log_cherez_regu = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert log_cherez_regu == 'Оформить заказ', "Не найдена кнопка Оформить заказ. Логирование через форму регистрации не произошло"
        print('Успешное логирование  через форму регистрации')

    def test_login_through_reset_password(self, driver):

        driver.find_element(*locator.PERSONAL_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.RESET_PASSWORD_BUTTON)))

        driver.find_element(*locator.EXIT_FROM_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_ENTRY_IN_OFFICE)))

        driver.find_element(*locator.LOGIN_FIELD).send_keys(TestEntrance.email)
        driver.find_element(*locator.PASSWORD).send_keys(TestEntrance.password)
        driver.find_element(*locator.BUTTON_ENTRY_IN_OFFICE).click()

        cherez_vostan_parol = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.BUTTON_PLACE_ORDER))).text
        assert cherez_vostan_parol == 'Оформить заказ',  "Не найдена кнопка Оформить заказ. Логирование через форму восстановления пароля не произошло"
        print('Успешное логирование через форму регистрации')
