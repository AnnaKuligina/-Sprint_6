from selenium.webdriver.common.by import By


class RentPageLocators:
    DATA_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")  # Поле для выбора срока аренды на странице "Про аренду"
    SELECT_TIME = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(2)")
    COLOR_BLACK = (By.ID, "black")  # Поле для выбора черного цвета самоката на странице "Про аренду"
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Поле для ввода комментария на странице "Про аренду"
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Middle__1CSJM:nth-child(2)")
    YES_BUTTON = (By.CSS_SELECTOR, "div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)")
    SEE_STATUS = (By.XPATH, ".// button[text() = 'Посмотреть статус']")
    CHECK_ORDER = (By.XPATH, ".//div[contains(text(), 'Самокат на складе')]")


class OrderPageLocators:
    PERSONAL_FORM = (By.XPATH), "//div[text()='Для кого самокат']"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")  # Поле для ввода имени на странице "Для кого самокат"
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")  # Поле для ввода фамилии на странице "Для кого самокат"
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")   # Поле для ввода адреса на странице "Для кого самокат"
    INPUT_METRO_ST = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле для ввода телефона на странице "Для кого самокат"
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")