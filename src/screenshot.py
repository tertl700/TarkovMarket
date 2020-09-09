from PIL import Image
from mss import mss


# screenshot main monitor using mss, convert to PIL image for processing
def capture():

    with mss() as sct:

        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

        img.save('images/screenshot.png')
