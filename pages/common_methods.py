from pycparser.c_ast import While
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from driver import Driver
from pages.base_page import BasePage

class CommonMethods(BasePage):
    AUTENTIFICARE_URL = 'https://www.saucedemo.com/'

    USER_INPUT = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="login-button"]')
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")
    ERROR_MESSAGE_LOCKED_USER = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    SIDE_MENIU = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    LOGOUT_BTN = (By.XPATH, '//*[@id="logout_sidebar_link"]')
    FILTER_BTN = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    A_TO_Z_OPTION = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[1]')
    PRODUCTS_NAME = (By.CLASS_NAME, 'inventory_item_name')
    PRICE_LOW_TO_HIGH_OPTION = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    PRODUCTS_PRICE = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_ADDED_TO_CART = (By.XPATH, "//div[@class='inventory_item_description'][.//div[text()='Sauce Labs Backpack']]//button[text()='Add to cart']")
    PRODUCT_ADDED_TO_CART_2nd = (By.XPATH, "//div[@class='inventory_item_description'][.//div[text()='Sauce Labs Bike Light']]//button[text()='Add to cart']")
    CART_BTN = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    PRODUCT_IN_CART = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    REMOVE_FROM_CART = (By.XPATH, "//button[text()='Remove']")
    CHECKOUT_BTN = (By.XPATH, '//*[@id="checkout"]')
    FIRST_NAME_INPUT = (By.XPATH, '//*[@id="first-name"]')
    LAST_NAME_INPUT = (By.XPATH, '//*[@id="last-name"]')
    ZIP_CODE_INPUT = (By.XPATH, '//*[@id="postal-code"]')
    CONTINUE_BTN = (By.XPATH, '//*[@id="continue"]')
    FINISH_BTN = (By.XPATH, '//*[@id="finish"]')
    SUCCESS_ORDER_MESSAGE = (By.XPATH, '//*[@id="checkout_complete_container"]/h2')
    PRICE_TOTAL_SECTION = (By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')


    BUTTONS = {
        'ERROR_MESSAGE': ERROR_MESSAGE,
        'ERROR_MESSAGE_LOCKED_USER': ERROR_MESSAGE_LOCKED_USER,
        'PRODUCT_IN_CART': PRODUCT_IN_CART,
        'SUCCESS_ORDER_MESSAGE': SUCCESS_ORDER_MESSAGE,
    }

    def check_if_element_is_present(self, element):
        """
        check_if_element_is_present("ERROR_MESSAGE")
        :param element:
        :return:
        """
        locator = self.BUTTONS.get(element)
        if locator:
            # by, selector = locator
            element_present = False
            while True:
                try:
                    self.wait_for_elem_presence(locator)
                    element_present = True
                    print(f"Print: Elementul a fost gasit!")
                    break
                except:
                    print(f"Print: Elementul nu este pe pagina.")
                    break
            assert element_present is True
        else:
            raise ValueError(f'Elementul "{element}" nu este definit in mapa BUTTONS')

    def check_if_element_is_not_present(self, element):
        """
        check_if_element_is_present("ERROR_MESSAGE")
        :param element:
        :return:
        """
        locator = self.BUTTONS.get(element)
        if locator:
            # by, selector = locator
            element_present = False
            while True:
                try:
                    self.wait_for_elem_presence(locator, 5)
                    element_present = True
                    print(f"Print: Elementul a fost gasit!")
                    break
                except:
                    print(f"Print: Elementul nu este pe pagina.")
                    element_present = False
                    break
            assert element_present is False
        else:
            raise ValueError(f'Elementul "{element}" nu este definit in mapa BUTTONS')

