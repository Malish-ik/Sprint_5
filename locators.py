from selenium.webdriver.common.by import By


class TestLocators:

    registration_link = By.XPATH, ".//a[contains(@class, 'Auth_link__1fOlj') and @href='/register']"  # зарегистрироваться
    registration_name = By.XPATH, ".//label[text()= 'Имя']/parent::div/input"  # имя при регистрации
    registration_email = By.XPATH, ".//label[text()= 'Email']/parent::div/input"  # email при регистрации
    registration_password = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"  # пароль при регистрации
    button_registration = By.XPATH, ".//button[text() = 'Зарегистрироваться']"  # кнопка Зарегистрироваться
    incorrect_password_error = By.XPATH, ".//p[@class= 'input__error text_type_main-default']"  # сообщение об ошибке
    button_enter_page_main = By.XPATH, ".//button[text() = 'Войти в аккаунт']"  # вход по кнопке «Войти в аккаунт» на главной
    personal_account_link = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/account']"  # Личный кабинет
    button_profile = By.XPATH, ".//a[text()='Профиль']" # кнопка Профиль в Личном кабинете
    header_burger = By.XPATH, ".//h1[text()='Соберите бургер']"  # заголовок Соберите бургеp
    logo_stellar_burgers = By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"  # логотип Stellar Burgers
    button_exit_personal_account = By.XPATH, ".//button[text()='Выход']"  # кнопка Выход в личном кабинете
    constructor_link = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href= '/']"  # Конструктор
    sauces_link = By.XPATH, ".//span[text() = 'Соусы']"  # раздел Соусы
    fillings_link = By.XPATH, ".//span[text() = 'Начинки']"  # раздел Начинки
    authorization_link = By.XPATH, ".//a[contains(@class, 'Auth_link__1fOlj') and @href='/login']"  # авторизоваться
    authorization_email = By.XPATH, ".//label[text()= 'Email']/parent::div/input"  # email при авторизации
    authorization_password = By.XPATH, ".//label[text()= 'Пароль']/parent::div/input"  # пароль при авторизации
    button_authorization = By.XPATH, ".//button[text()= 'Войти']"  # кнопка Войти в форме авторизации
    button_order = By.XPATH, ".//button[text()= 'Оформить заказ']"  # кнопка Оформить заказ
    header_enter = By.XPATH, ".//h2[text()= 'Вход']"  # заголовок 'Вход'
    forgot_password_link = By.XPATH, ".//a[contains(@class, 'Auth_link__1fOlj') and @href='/forgot-password']"  # восстановить пароль
    bun_name = By.XPATH, ".//p[text()= 'Флюоресцентная булка R2-D3']"  # булка
    sauce_name = By.XPATH, ".//p[text()= 'Соус Spicy-X']"  # соус
    filling_name = By.XPATH, ".//p[text()= 'Мясо бессмертных моллюсков Protostomia']"  # начинка
