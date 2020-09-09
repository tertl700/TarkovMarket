import asyncio
import keyboard
from src import globals, screenshot, item_price

HOTKEY = "CTRL+Z"

async def main():
    try:
        print("Starting puppeteer...")
        await globals.init()
        # Collect events until released
        print ("Inspect an item and press CTRL+Z to start")
        while True:
            keyboard.wait(HOTKEY)
            screenshot.capture()
            await item_price.fetch_price()
    except Exception as e:
        raise
    finally:
        await globals.browser.close()

if __name__ == "__main__":
    asyncio.run(main())
