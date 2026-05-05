from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class Driver:
    def __init__(self, browser="chrome"):
        self.driver = self._create(browser)

    def _create(self, browser):

        if browser == "chrome":
            options = ChromeOptions()
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
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            # dezactiveaza password manager
            options.set_preference("signon.rememberSignons", False)
            # dezactiveaza notificari
            options.set_preference("dom.webnotifications.enabled", False)
            # dezactiveaza autofill
            options.set_preference("extensions.formautofill.addresses.enabled", False)
            options.set_preference("extensions.formautofill.creditCards.enabled", False)
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()

        elif browser == "edge":
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--log-level=3")
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Browser necunoscut: {browser}")

        driver.implicitly_wait(0)
        driver.set_page_load_timeout(30)

        driver.get("https://www.saucedemo.com/")

        return driver

    def restart(self, browser="chrome"):
        self.close()
        self.driver = self._create(browser)

    def close(self):
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass