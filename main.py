import asyncio
import keyboard
from src import globals, screenshot, item_price
async def main():
    try:
        await globals.init()
        # Collect events until released
        print ("Running...")
        while True:
            keyboard.wait('ctrl+\\')
            screenshot.capture()
            await item_price.fetch_price()
    except Exception as e:
        raise
    finally:
        await globals.browser.close()

if __name__ == "__main__":
    asyncio.run(main())