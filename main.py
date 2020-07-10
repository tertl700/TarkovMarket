import asyncio

from pynput import keyboard

from src.item_id import on_press

async def main():
    # Collect events until released
    print ("Running...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    asyncio.run(main())