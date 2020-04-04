import pyscreenshot as ImageGrab
from pynput import keyboard
import key_price


def on_press(key):
    try:
        key_str = 'alphanumeric key {0} pressed'.format(key.char)
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        if(key == keyboard.Key.page_up):
            screenshot()
            #img_processing.run()
            key_price.main()
        elif(key == keyboard.Key.page_down):
            key_price.driver.quit()
            exit()

def screenshot():   
    im = ImageGrab.grab(bbox=(850,380,1600,405))
    im.save('images/key.png')

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

