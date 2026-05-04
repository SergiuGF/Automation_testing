from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from driver import Driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def go_to(self, page):
        return self.driver.get(page)
    def go_back(self):
        return self.driver.back()
    def find(self, locator):
        return self.driver.find_element(*locator)
    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)
    def click(self, locator):
        self.find(locator).click()
    def wait_and_click(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
    def click_if_contains_text(self, locator, text):
        element = self.find(locator)
        if text in element.text:
            element.click()
        else:
            pass
    def type(self, locator, text):
        if text == "N/A":
            pass
        else:
            self.find(locator).send_keys(text)

    def wait_and_type(self, locator, text, timeout=30, clear=True):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        if clear:
            element.clear()
        element.send_keys(text)
    def search_and_enter(self, locator, product_name):
        search_input = self.find(locator)
        search_input.send_keys(product_name)
        search_input.send_keys(Keys.ENTER)
    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()
    def is_element_not_displayed(self, locator):
        try:
            return not self.find(locator).is_displayed()
        except NoSuchElementException:
            # The element was not found, so it is considered not to be displayed
            return True
    def get_text(self, locator):
        return self.find(locator).text
    def get_text_multiple(self, locator):
        return self.find_multiple(locator).text
    def get_attribute(self, element, attribute_name):
        try:
            return element.get_attribute(attribute_name)
        except NoSuchElementException:
            # Handle NoSuchElementException if element is not found
            return None
    def select_dropdown_option_by_text(self, dropdown_locator, text):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)
    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)
        if not checkbox_element.is_selected():
            self.click(checkbox_locator)
    def current_url(self):
        return self.driver.current_url
    def wait_for_element_visibile(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, selector)))
    def wait_for_elem_presence(self, selector, timeout=30):
        WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(EC.presence_of_element_located(selector))
    def wait_for_elem_clickable(self, selector, timeout=30):
        WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(EC.element_to_be_clickable(selector))
    def wait_for_elements_presence(self, selector, timeout=30):
        WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(EC.presence_of_all_elements_located(selector))


    def click_if_present_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            try:
                self.wait_scroll_and_click_elem_by_selector(by, selector)
            except TimeoutException:
                print(f"Element identified by '{selector}' did not become clickable within the specified timeout.")
    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)