import random
import locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransition:
    def test_perehod_po_lk(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в форму входа проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ)))

        # переход в лк когда мы авторизованы
        driver.find_element(*locator.LICNY_CABINET).click()

        lk = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ISTORI_ZAKAZ))).text
        assert lk == 'История заказов'

        driver.quit()

    def test_perehod_v_konstruktor_i_logo(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в форму входа проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ)))

        # переход в лк когда мы авторизованы
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ISTORI_ZAKAZ)))

        # переход из лк когда авторизованы в конструктор
        driver.find_element(*locator.KONSTR).click()

        konstrukt = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert konstrukt == 'Оформить заказ'

        #переход из лк когда авторизованы в логотип
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ISTORI_ZAKAZ)))
        driver.find_element(*locator.LOGO).click()

        # проверяем что открылся логотип
        logo = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ))).text
        assert logo == 'Оформить заказ'

        driver.quit()

    def test_vshod_iz_lk(self, driver):
        email = "Fursov_08@ya.ru"
        password = 'йцу123йцу'

        # зашли в форму входа проверили что загрузилось
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE)))

        # заполняем поля для входа. кликаем на авторизацию,  проверили что вошли
        driver.find_element(*locator.LOGIN).send_keys(email)
        driver.find_element(*locator.PASSWORD).send_keys(password)
        driver.find_element(*locator.KNOPKA_VHODA_V_KABINETE).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ZAKAZ)))

        #переходим в лк
        driver.find_element(*locator.LICNY_CABINET).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.ISTORI_ZAKAZ)))

        # нажимаем выход. проверяем что вышли.
        driver.find_element(*locator.VIHOD_IZ_PROFIL).click()
        exit = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locator.KNOPKA_VHODA_V_KABINETE))).text
        assert exit == 'Войти'

        driver.quit()


    def test_konsrtuktor_perehod_k_razdelam(self, driver):

        #нажали на соусы  проверили что проскролилась( класс кнопки меняется при нажатии или скролле)
        element_sause = driver.find_element(*locator.SAUSE)
        driver.execute_script("arguments[0].scrollIntoView();", element_sause)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locator.SAUSE_CLIK)))

        #нажали на начинки  проверили что проскролилось(класс кнопки меняется при нажатии или скролле)
        element_nachin = driver.find_element(*locator.NASCINK)
        driver.execute_script("arguments[0].scrollIntoView();", element_nachin)
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((locator.NASCINK_CLIK)))

        #нажали на булки проверили что проскролилось (класс кнопки меняется при нажатии или скролле)
        element_bulka = driver.find_element(*locator.BULKA)
        driver.execute_script("arguments[0].scrollIntoView();", element_bulka)
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locator.BULKA_KLIK)))

        driver.quit()
