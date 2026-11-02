from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопка "Лента Заказов"
    top_orders_button = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Лента Заказов']")

    # Кнопка "Конструктор"
    top_constructor_button = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va ml-2') and text()='Конструктор']")

    # Надпись "Соберите бургер" 
    header1 = (By.XPATH, "//h1[contains(@class, 'text text_type_main-large mb-5 mt-10') and text()='Соберите бургер']")

    # Надпись "Лента заказов" 
    header2 = (By.XPATH, "//h1[contains(@class, 'text text_type_main-large mt-10 mb-5') and text()='Лента заказов']")

    # Ингредиент (булка)
    ingredient = (By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and text()='Флюоресцентная булка R2-D3']")

    # Кнопка закрытия модального окна
    close_modal_button = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")

    # Счетчик ингредиента (булка)
    counter = (By.XPATH, "//p[contains(@class, 'counter_counter__num__3nue1')]")

    # Конструктор бургеров
    constructor_field = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")

    # Заказы за всё время
    all_orders = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    # Заказы за сегодня
    today_orders = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")

    # Заказы в работе
    orders_in_progress = (By.XPATH, "//li[contains(@class, 'text text_type_digits-default mb-2')]")

    # Модальное окно
    modal_window = (By.XPATH, "//div[contains(@class, 'Modal')]")