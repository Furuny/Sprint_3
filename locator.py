
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# личный кабинет
PERSONAL_AREA = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
# кнопка войти в личном кабинете(форме входа)
BUTTON_ENTRY_IN_OFFICE = (By.XPATH, "//button[contains(text(),'Войти')]")
# форма входа. кнопка перехода на форму регистрации
BUTTON_GO_REGISTRATION = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
# форма регистрации. кнопка зарегестрироваться
BUTTON_REGISTER = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
# форма регистрации поле имени
NAME_FIELD = (By.XPATH, "//fieldset[1]//input")
# форма регистрации поле почты
MAIL_FIELD = (By.XPATH, "//fieldset[2]//input")
# форма регистрации поле пароля
PASSWORD_FIELD = (By.XPATH, "//fieldset[3]//input")
# уведомление при ошибке в пароле
PASSWORD_ERROR_NOTIFICATION = (By.XPATH,"//p[contains(text(),'Некорректный пароль')]")
# кнопка войти в аккаунт на главной
LOG_IN_ACCOUNT_FROM_MAIN = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
# поле логина(почты) на форме входа(личный кабинет)
LOGIN_FIELD = (By.XPATH,"//fieldset[1]//input")
# поле пароля на форме входа (личный кабинет)
PASSWORD = (By.XPATH,"//fieldset[2]//input")
# кнопка оформить заказ на главной( появляется когда авторизовались)
BUTTON_PLACE_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
#кнопка войти для выхода с формы регистрации обратно на форму авторизации
EXIT_FROM_REGISTRATION = (By.XPATH, "//a[contains(text(),'Войти')]")
#кнопка восстановления пароля в форме входа (личный кабинет)
PASSWORD_RECOVERY = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
# кнопка восстановить пароль на форме восстановления пароля
RESET_PASSWORD_BUTTON  = (By.XPATH, "//button[contains(text(),'Восстановить')]")
# история заказов в личном кабинете когда авторизованы
ORDER_HISTORY = (By.XPATH, "//a[contains(text(),'История заказов')]")
#конструктор бургеров на главной
BURGER_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
# логотип сверху по центру
LOGO = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")
#кнопка выхода из профиля
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
#кнопка с выбором соуса
SAUCE = (By.XPATH, "//p[contains(text(),'Соус фирменный Space Sauce')]")
#кнопка соусы после нажатия или скрола
SAUCE_CHOSEN = (By.XPATH, "//section[1]/div[1]/div[2][contains(@class,'tab_tab_type_current__2BEPc')]")
#кнопка с выбором начинки
FILLING_CHEEZE = (By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
#кнопка начинки после нажатия или скрола
FILLING_CHOSEN = (By.XPATH, "//section[1]/div[1]/div[3][contains(@class,'tab_tab_type_current__2BEPc')]")
#кнопка с выбором булки
BUN = (By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")
#кнопка булка после нажатия или скрола
BUN_CHOSEN = (By.XPATH, "//section[1]/div[1]/div[1][contains(@class,'tab_tab_type_current__2BEPc')]")
