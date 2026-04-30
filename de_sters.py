# driver.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless=False):
    options = Options()

    # UI
    options.add_argument("--start-maximized")

    # stabilitate
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")

    # headless (optional)
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    # IMPORTANT: evităm implicit wait
    driver.implicitly_wait(0)

    return driver