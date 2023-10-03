from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group .btn-default:nth-child(1)")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MASSAGE_BOOK_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    MASSAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    MASSAGE_EMPTY = (By.CSS_SELECTOR, ".content #content_inner p a")
    ITEMS_FORM = (By.CSS_SELECTOR, ".basket_summary")
    NOT_EMPTY_MASSAGE = "voucher"
