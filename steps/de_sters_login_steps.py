from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# @then("suma preturilor este egala cu cea afisata la rubrica suma total (Price Total)")
def step_impl(context):

    element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located(CommonMethods.PRICE_TOTAL_SECTION)
    )

    total_text = element.text

    # "Item total: $29.99" -> 29.99
    total_displayed = float(total_text.split("$")[1])

    assert round(context.total_products, 2) == round(total_displayed, 2), \
        f"Suma calculata {context.total_products} != suma afisata {total_displayed}"