from asyncio import get_event_loop, new_event_loop
from src.item_price import main
from PIL import Image
from pynput import keyboard
from mss import mss


# on pg_up, get item_id and check item_price. on pg_down exit script
def on_press(key):
    if key == keyboard.Key.page_up:
        screenshot()
        new_event_loop().run_until_complete(main())



# screenshot main monitor using mss, convert to PIL image for processing
def screenshot():

    with mss() as sct:

        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

        img.save('images/screenshot.png')
