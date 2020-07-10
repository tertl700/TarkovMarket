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

    await search_bar.type(item_name)
    await page.waitForXPath(f"//span[contains(text(),'{item_name}')]")
    price_element = await page.waitForSelector("span.price-main")
    price = await page.evaluate(
        "(element) => element.textContent", price_element
    )

    print(f"Price is: {price}")


# trader = driver.find_element_by_class_name('item-card')
# print(trader)

# img_processing.log_image(result)
