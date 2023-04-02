
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# личный кабинет
LICNY_CABINET = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
# кнопка войти в личном кабинете(форме входа)
KNOPKA_VHODA_V_KABINETE = (By.XPATH, "//button[contains(text(),'Войти')]")
# форма входа. кнопка перехода на форму регистрации
REGISTRACIA = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
# форма регистрации. кнопка зарегестрироваться
ZAREGISTRIROVATSA = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
# форма регистрации поле имени
REGA_NAME = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
# форма регистрации поле почты
REGA_MAIL = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
# форма регистрации поле пароля
REGA_PASS = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]")
# уведомление при ошибке в пароле
EROR = (By.XPATH,"//p[contains(text(),'Некорректный пароль')]")
# кнопка войти в аккаунт на главной
VOITI_V_AK_S_GLAVNOI = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
# поле логина(почты) на форме входа(личный кабинет)
LOGIN = (By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
# поле пароля на форме входа (личный кабинет)
PASSWORD = (By.XPATH,"//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
# кнопка оформить заказ на главной( появляется когда авторизовались)
ZAKAZ = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
#кнопка войти для выхода с формы регистрации обратно на форму авторизации
VIHOD_S_REGI = (By.XPATH, "//a[contains(text(),'Войти')]")
#кнопка восстановления пароля в форме входа (личный кабинет)
VOST_PAROL = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
# кнопка восстановить пароль на форме восстановления пароля
KNOPKA_VOST_PAROL = (By.XPATH, "//button[contains(text(),'Восстановить')]")
# история заказов в личном кабинете когда авторизованы
ISTORI_ZAKAZ = (By.XPATH, "//a[contains(text(),'История заказов')]")
#конструктор бургеров на главной
KONSTR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
# логотип сверху по центру
LOGO = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")
#кнопка выхода из профиля
VIHOD_IZ_PROFIL = (By.XPATH, "//button[contains(text(),'Выход')]")
#кнопка с выбором соуса
SAUSE = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[2]/ul[2]/a[4]/img[1]")
#кнопка соусы после нажатия или скрола
SAUSE_CLIK = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2)/*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
#кнопка с выбором начинки
NASCINK = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[2]/ul[3]/a[8]/img[1]")
#кнопка начинки после нажатия или скрола
NASCINK_CLIK = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2)/*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
#кнопка с выбором булки
BULKA = (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[2]/ul[1]/a[1]/img[1]")
#кнопка булка после нажатия или скрола
BULKA_KLIK = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 > div:nth-child(2)/*[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")