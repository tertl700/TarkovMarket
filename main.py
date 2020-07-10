import asyncio
import src.globals as globals
import keyboard
import src.item_id

async def main():
    try:
        await globals.init()
        # Collect events until released
        print ("Running...")
        while True:
            keyboard.wait('left shift')
            await src.item_id.fetch_price()
    except Exception as e:
        raise
    finally:
        await globals.browser.close()

if __name__ == "__main__":
    asyncio.run(main())