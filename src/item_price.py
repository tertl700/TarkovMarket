import src.globals as globals
from src.img_processing import run
import os
from pyppeteer.errors import TimeoutError
# make directory for storing images if it does not exist in path
if not os.path.exists("images"):
    os.makedirs("images")


async def fetch_price():
    page = globals.page
    search_bar = await page.querySelector('.search input[type="text"]')
    item_name = run()

    await page.evaluate("""
    () => { const input = document.querySelector('.search input[type="text"]');
    input.value = '';
    }""")
    await search_bar.type(item_name)
    if not await does_item_exist(page, item_name):
        print(f"Could not find item: {item_name}")
        return

    main_price = await get_text_from_selector("span.price-main")
    price_per_slot = await get_text_from_selector("span.price-sec")
    print(f"Item name: {item_name}")
    print(f"Price is: {main_price}")
    print(f"Price per slot: {price_per_slot}")

async def does_item_exist(page, item_name):
    try:
        await page.waitForXPath(f"//span[contains(text(),'{item_name}')]", options={"timeout": 3000} )
        return True
    except TimeoutError:
        return False

async def get_text_from_selector(selector):
    page = globals.page
    element = await page.querySelector(selector)
    if not element:
        return "N/A"

    text = await page.evaluate(
        "(element) => element.textContent", element
    )

    return text.strip(' \n\r')
