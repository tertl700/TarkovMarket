import src.globals as globals
from src.img_processing import run
import os

# make directory for storing images if it does not exist in path
if not os.path.exists("images"):
    os.makedirs("images")


async def fetch_price():
    page = globals.page
    search_bar = await page.querySelector('.search input[type="text"]')
    item_name = run()
    print(f"item name: {item_name}")

    await page.evaluate("""
    () => { const input = document.querySelector('.search input[type="text"]');
    input.value = '';
    }""")
    await search_bar.type(item_name)
    await page.waitForXPath(f"//span[contains(text(),'{item_name}')]")
    main_price = await get_text_from_selector("span.price-main")
    price_per_slot = await get_text_from_selector("span.price-sec")
    print(f"Price is: {main_price}")
    print(f"Price per slot: {price_per_slot}")

async def get_text_from_selector(selector):
    page = globals.page
    element = await page.querySelector(selector)
    if not element:
        return "N/A"

    text = await page.evaluate(
        "(element) => element.textContent", element
    )

    return text.strip(' \n\r')

# trader = driver.find_element_by_class_name('item-card')
# print(trader)

# img_processing.log_image(result)
