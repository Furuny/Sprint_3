import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEntrance:
    def test_vhod_s_glavnoi(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в форму входа проверили что загрузилось
        driver.find_element(*locator.VOITI_V_AK_S_GLAVNOI).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        log_s_glavn = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert log_s_glavn == 'Оформить заказ'
        driver.quit()

    def test_vhod_cherez_lk(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в лк проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))


        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()


        log_cherez_lk = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert log_cherez_lk == 'Оформить заказ'

        driver.quit()

    def test_vhod_cherez_regu(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'
        # зашли в лк проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заходим в форму регистрации проверям что прогрузилось
        driver.find_element(*locator.REGISTRACIA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.VIHOD_S_REGI)))

        # переходим из формы регистрации обратно на форму входа по кнопке войти. проверям что переход произошел
        driver.find_element(*locator.VIHOD_S_REGI).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        log_cherez_regu = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert log_cherez_regu == 'Оформить заказ'
        driver.quit()

    def test_vhod_cherez_vostan_parol(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в лк проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заходим в форму восстановления пароля, проверям что прогрузилось
        driver.find_element(*locator.VOST_PAROL).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VOST_PAROL)))

        # переходим из формы восстановления пароля обратнона форму входа по кнопке войти. проверям что переход произошел
        driver.find_element(*locator.VIHOD_S_REGI).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        cherez_vostan_parol = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert cherez_vostan_parol == 'Оформить заказ'
        driver.quit()
