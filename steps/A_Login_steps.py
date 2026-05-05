from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.common_methods import CommonMethods

"""@Login_001"""
@given("utilizatorul se afla pe Pagina de Autentificare")
def step_impl(context):
    context.browser.get("https://www.saucedemo.com/")
@when('se insereaza credentiale valide in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN')
def step_impl(context):
    context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "standard_user")
    context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
    context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
@then("utilizatorul este autentificat cu succes si este directionat pe Pagina Principala")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    assert context.browser.current_url == "https://www.saucedemo.com/inventory.html"

    #posibil se poate sterge urmatorul cod:
    # # Se creaza conditiile pentru urmatorul scenariu
    # context.browser.get(CommonMethods.AUTENTIFICARE_URL)

"""@Login_002"""
# given a fost deja definit
@when("se insereaza credentiale invalide in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN")
def step_impl(context):
    context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "invalid_user")
    context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "invalid_password")
    context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
@then("pe ecran este afisat un mesaj de eroare care indica faptul ca datele inserate nu sunt valide")
def step_impl(context):
    context.common_methods.check_if_element_is_present('ERROR_MESSAGE')

"""@Login_003"""
@given('utilizatorul se afla pe Pagina Principala')
def step_impl(context):
    try:
        context.common_methods.wait_for_elem_presence(CommonMethods.APP_LOGO, 3)
        context.browser.get(CommonMethods.MAIN_PAGE_URL)
    except:
        context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "standard_user")
        context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
        context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
@when('se actioneaza butonul de tip burger din partea stanga-sus, iar din optiunile alese se actioneaza butonul LOGOUT')
def step_iml(context):
    # posibil se poate sterge codul cu alerta
    # try:
    #     WebDriverWait(context.browser, 10, 0.5).until(EC.alert_is_present())
    #     alert = context.browser.switch.to.alert
    #     alert.accept()
    #     print(f"print: Alerta acceptata.")
    # except:
    #     print(f"print: Alerta nu a fost afisata.")

    context.common_methods.wait_and_click(CommonMethods.SIDE_MENIU)
    context.common_methods.wait_for_elem_clickable(CommonMethods.LOGOUT_BTN, 10)
    context.common_methods.wait_and_click(CommonMethods.LOGOUT_BTN)
@then('utilizatorul este deautentificat si este directionat catre Pagina de Autentificare')
def step_iml(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://www.saucedemo.com/")
    )
    assert context.browser.current_url == "https://www.saucedemo.com/"

"""@Login_004"""
# given a fost deja definit
@when('se insereaza credentiale unui utilizator care a fost BLOCAT in campurile USERNAME, respectiv PASSWORD si se actioneaza butonul LOGIN')
def step_iml(context):
    context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "locked_out_user")
    context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
    context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
@then("pe ecran este afisat un mesaj de eroare care indica faptul ca utilizatorul a fost BLOCAT")
def step_impl(context):
    context.common_methods.wait_for_elem_presence(CommonMethods.ERROR_MESSAGE_LOCKED_USER, 5)
    context.common_methods.check_if_element_is_present('ERROR_MESSAGE_LOCKED_USER')

