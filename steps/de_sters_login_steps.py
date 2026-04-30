from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("suma produselor este corecta in cos")
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    # 🔹 locator pentru prețuri produse
    price_locator = (By.CLASS_NAME, "inventory_item_price")

    elements = wait.until(
        EC.presence_of_all_elements_located(price_locator)
    )

    # 🔹 extragi și calculezi suma
    prices = [
        float(el.text.replace("$", ""))
        for el in elements
    ]

    total_products = sum(prices)

    # 🔹 locator total
    total_locator = (By.CLASS_NAME, "summary_subtotal_label")

    total_text = wait.until(
        EC.visibility_of_element_located(total_locator)
    ).text

    # "Item total: $29.99" -> 29.99
    total_displayed = float(total_text.split("$")[1])

    # 🔥 assert
    assert total_products == total_displayed, \
        f"Suma calculata {total_products} != suma afisata {total_displayed}"