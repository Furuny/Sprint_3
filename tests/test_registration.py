import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    def test_rega(self, driver):
        name = 'Andrew'
        random_number = random.randint(1000, 9999)
        email = "Fursov_08_" + str(random_number) +"@ya.ru"
        password = 'qwe123'


        #зашли в лк проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        #перешли на форму зарегестироваться, проверили что прогрузилось
        driver.find_element(*locator.REGISTRACIA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAREGISTRIROVATSA)))

        #заполнили поля, зарегестрировались проверили что перешли на след экран
        driver.find_element(*locator.REGA_NAME).send_keys(name)
        driver.find_element(*locator.REGA_MAIL).send_keys(email)
        driver.find_element(*locator.REGA_PASS).send_keys(password)
        driver.find_element(*locator.ZAREGISTRIROVATSA).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        #проверяем что регистрация прошла.
        reg = driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).text
        assert reg == 'Войти'

        driver.quit()


    def test_eroor_password(self,driver):
        name = 'Andrew'
        random_number = random.randint(1000, 9999)
        email = "Fursov_08_" + str(random_number) + "@ya.ru"


        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))


        driver.find_element(*locator.REGISTRACIA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAREGISTRIROVATSA)))

        driver.find_element(*locator.REGA_NAME).send_keys(name)
        driver.find_element(*locator.REGA_MAIL).send_keys(email)
        driver.find_element(*locator.REGA_PASS).send_keys('123qw')
        driver.find_element(*locator.ZAREGISTRIROVATSA).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator.EROR))

        # проверяем что уведомление появилось
        eror = driver.find_element(*locator.EROR).text
        assert eror == 'Некорректный пароль'

        driver.quit()
