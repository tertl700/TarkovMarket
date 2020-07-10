from src.img_processing import run
import os
from pyppeteer import launch

# make directory for storing images if it does not exist in path
if not os.path.exists("images"):
    os.makedirs("images")


async def main():
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False
    )
    page = await browser.newPage()
    await page.goto("https://tarkov-market.com/")

    search_bar = await page.querySelector('.search input[type="text"]')
    item_name = run()
    print(f"item name: {item_name}")

    await search_bar.type(item_name)
    await page.waitFor(1000)
    price_element = await page.querySelector("span.price-main")
    price = await price_element.evaluate(
        "(element) => element.textContent", price_element
    )

    print(price)


# trader = driver.find_element_by_class_name('item-card')
# print(trader)

# img_processing.log_image(result)
