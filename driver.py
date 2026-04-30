from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest

class Driver:
    def __init__(self):

        options = Options()

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")

        # pentru popup Google
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)

        # trimitem options aici
        self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(0)
        self.driver.get("https://www.saucedemo.com/")



    def restart(self):
        self.close()
        self.__init__()

    def close(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass