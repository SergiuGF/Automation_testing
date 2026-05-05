from driver import Driver
# from pages.login_page import LoginPage
from pages.common_methods import CommonMethods

def before_all(context):
    browser = context.config.userdata.get("browser", "chrome")
    context.driver_wrapper = Driver(browser)

def before_scenario(context, scenario):
    # driverul este intotdeauna cel activ
    context.browser = context.driver_wrapper.driver
    # rebind pagini (OBLIGATORIU dupa restart)
    # context.functional = FunctionalitatiGenerale(context.browser)
    context.common_methods = CommonMethods(context.browser)

def after_all(context):
    context.driver_wrapper.close()

def restart_driver(context):
    context.driver_wrapper.restart()
    # CRITIC: actualizezi referintele
    context.browser = context.driver_wrapper.driver
    # context.functional = FunctionalitatiGenerale(context.browser)
    context.common_methods = CommonMethods(context.browser)