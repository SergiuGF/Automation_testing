from time import sleep

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.common_methods import CommonMethods

"""@FG_005"""
# given a fost deja defin
@when("se actioneaza butonul FILTRE si se alege optiunea A to Z")
def step_impl(context):
    context.common_methods.wait_and_click(CommonMethods.FILTER_BTN)
    context.common_methods.wait_and_click(CommonMethods.A_TO_Z_OPTION)
@then("produsele afisate pe pagina sunt sortate in ordine alfabetica")
def step_impl(context):
    # așteaptă să existe elementele
    elements = WebDriverWait(context.browser, 10).until(
        EC.presence_of_all_elements_located(CommonMethods.PRODUCTS_NAME)
    )
    # extrage textele
    product_names = [el.text for el in elements]
    assert product_names == sorted(product_names), \
        f"Lista NU este sortată: {product_names}"
@when("se actioneaza butonul FILTRE si se alege optiunea PRICE low to high")
def step_impl(context):
    context.common_methods.wait_and_click(CommonMethods.FILTER_BTN)
    context.common_methods.wait_and_click(CommonMethods.PRICE_LOW_TO_HIGH_OPTION)
@then("produsele afisate pe pagina sunt sortate in ordine crescatoare in functie de pret")
def step_impl(context):
    # așteaptă să existe elementele
    elements = WebDriverWait(context.browser, 10).until(
        EC.presence_of_all_elements_located(CommonMethods.PRODUCTS_PRICE)
    )
    # extragem prețurile și le convertim în float
    prices = []
    for el in elements:
        text = el.text.replace("$", "")  # "$29.99" -> "29.99"
        prices.append(float(text))
    print(f"Print: prices: {prices}")
    # verificăm sortarea
    assert prices == sorted(prices), \
        f"Prețurile NU sunt sortate crescător: {prices}"

"""@FG_006"""
# given a fost deja definit
@when("se actioneaza butonul ADD TO CART aferent produsului de interes")
def step_impl(context):
    context.common_methods.wait_and_click(CommonMethods.PRODUCT_ADDED_TO_CART)
@then('produsul de referinta se afla in cosul de cumparaturi')
def step_impl(context):
    sleep(3)
    context.common_methods.wait_and_click(CommonMethods.CART_BTN)
    context.common_methods.wait_for_elem_presence(CommonMethods.PRODUCT_IN_CART, 5)
    context.common_methods.check_if_element_is_present('PRODUCT_IN_CART')
    sleep(3)
    # se creaza conditiile pentru scenariul urmator
    context.common_methods.wait_and_click(CommonMethods.REMOVE_FROM_CART)


"""@FG_007"""
@given('utilizatorul se afla pe Pagina Cosului de cumparaturi unde are adaugat cel putin un produs')
def step_impl(context):
    try:
        context.common_methods.wait_for_elem_presence(CommonMethods.APP_LOGO, 3)
        context.browser.get(CommonMethods.MAIN_PAGE_URL)
    except:
        context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "standard_user")
        context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
        context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
    context.common_methods.wait_and_click(CommonMethods.PRODUCT_ADDED_TO_CART)
    context.common_methods.wait_and_click(CommonMethods.CART_BTN)
@when('se actioneaza butonul REMOVE aferent produsului de interes')
def step_impl(context):
    while True:
        try:
            context.common_methods.wait_for_elem_presence(CommonMethods.REMOVE_FROM_CART, 5)
            context.common_methods.wait_and_click(CommonMethods.REMOVE_FROM_CART)
        except:
            break

@then('produsul de referinta NU se mai afla in cosul de cumparaturi')
def step_impl(context):
    context.common_methods.check_if_element_is_not_present('PRODUCT_IN_CART')

"""@FG_008"""
@given("in cosul de cumparaturi sunt adaugate cel putin doua produse")
def step_impl(context):
    try:
        context.common_methods.wait_for_elem_presence(CommonMethods.APP_LOGO, 3)
        context.browser.get(CommonMethods.MAIN_PAGE_URL)
    except:
        context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "standard_user")
        context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
        context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
    context.common_methods.wait_and_click(CommonMethods.PRODUCT_ADDED_TO_CART)
    context.common_methods.wait_and_click(CommonMethods.PRODUCT_ADDED_TO_CART_2nd)
    context.common_methods.wait_and_click(CommonMethods.CART_BTN)

@when("se aduna preturile produselor pentru a obtine suma acestora si se urmeaza pasii pentru finalizarea comenzii pana in pasul in care este afisata suma total (Price Total)")
def step_impl(context):
    context.elements = WebDriverWait(context.browser, 10).until(
        EC.presence_of_all_elements_located(CommonMethods.PRODUCTS_PRICE)
    )
    prices = [
        float(el.text.replace("$", ""))
        for el in context.elements
    ]
    context.total_products = sum(prices)

    context.common_methods.wait_and_click(CommonMethods.CHECKOUT_BTN)
    context.common_methods.wait_and_type(CommonMethods.FIRST_NAME_INPUT, "FIRST_NAME")
    context.common_methods.wait_and_type(CommonMethods.LAST_NAME_INPUT, "LAST_NAME")
    context.common_methods.wait_and_type(CommonMethods.ZIP_CODE_INPUT, "123456")
    context.common_methods.wait_for_elem_clickable(CommonMethods.CONTINUE_BTN, 5)
    context.common_methods.wait_and_click(CommonMethods.CONTINUE_BTN, 5)
@then("suma preturilor este egala cu cea afisata la rubrica suma total (Price Total)")
def step_impl(context):
    element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(CommonMethods.PRICE_TOTAL_SECTION)
    )
    total_text = element.text
    # "Item total: $29.99" -> 29.99
    total_displayed = float(total_text.split("$")[1])
    # 🔥 assert
    assert context.total_products == total_displayed, \
        f"Suma calculata {context.total_products} != suma afisata {total_displayed}"
    # se creaza conditiile pentru scenariul urmator
    while True:
        context.browser.get(CommonMethods.CART_URL)
        try:
            context.common_methods.wait_for_elem_presence(CommonMethods.REMOVE_FROM_CART, 5)
            context.common_methods.wait_and_click(CommonMethods.REMOVE_FROM_CART)
        except:
            break

"""@FG_009"""
@given("in cosul de cumparaturi este adaugat cel putin un produs")
def step_impl(context):
    try:
        context.common_methods.wait_for_elem_presence(CommonMethods.APP_LOGO, 3)
        context.browser.get(CommonMethods.MAIN_PAGE_URL)
    except:
        context.common_methods.wait_and_type(CommonMethods.USER_INPUT, "standard_user")
        context.common_methods.wait_and_type(CommonMethods.PASSWORD_INPUT, "secret_sauce")
        context.common_methods.wait_and_click(CommonMethods.LOGIN_BTN)
    context.common_methods.wait_and_click(CommonMethods.PRODUCT_ADDED_TO_CART)
    context.common_methods.wait_and_click(CommonMethods.CART_BTN)
@when("se actioneaza butonul Checkout")
def step_impl(context):
    context.common_methods.wait_and_click(CommonMethods.CHECKOUT_BTN)
@then("utilizatorul este directionat catre pagina in care este solicitata furnizarea datelor personale (nume, prenume si cod postal)")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://www.saucedemo.com/checkout-step-one.html")
    )
    assert context.browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"
@when("se insereaza datele personale in campurile aferente (nume, prenume si cod postal) si se actioneaza butonul Continue")
def step_impl(context):
    context.common_methods.wait_and_type(CommonMethods.FIRST_NAME_INPUT, "FIRST_NAME")
    context.common_methods.wait_and_type(CommonMethods.LAST_NAME_INPUT, "LAST_NAME")
    context.common_methods.wait_and_type(CommonMethods.ZIP_CODE_INPUT, "123456")
    context.common_methods.wait_for_elem_clickable(CommonMethods.CONTINUE_BTN, 5)
    context.common_methods.wait_and_click(CommonMethods.CONTINUE_BTN, 5)
@then("utilizatorul este directionat catre pagina de previzualizare a comenzii")
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html")
    )
    assert context.browser.current_url == "https://www.saucedemo.com/checkout-step-two.html"
@when("se actioneaza butonul Finish")
def step_impl(context):
    context.common_methods.wait_and_click(CommonMethods.FINISH_BTN, 5)
@then("pe ecran este afisat un mesaj care indica faptul ca procesul a fost finalizat cu succes")
def step_impl(context):
    context.common_methods.check_if_element_is_present('SUCCESS_ORDER_MESSAGE')

