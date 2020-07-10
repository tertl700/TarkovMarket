from selenium import webdriver
import img_processing
import time
import os


# make directory for storing images if it does not exist in path
if not os.path.exists('images'):
    os.makedirs('images')

# hide mozilla
os.environ['MOZ_HEADLESS'] = '1'

# start selenium driver for firefox and open main page of tarkov-market
driver = webdriver.Firefox()
driver.get("https://tarkov-market.com")
print('Ready')


# find search bar and enter text from img_processing
def main():

    global driver
    
    search_bar = driver.find_element_by_css_selector("input[placeholder='Search'")
    search_bar.clear()
    search_bar.send_keys(img_processing.run())
    time.sleep(2.5)
    
    try:

        item_price = driver.find_element_by_class_name('price-main')
        print(f'Flea: {item_price.text}')
        result = True

    except:

        print('No price detected')
        print('logged broken crop')
        result = False

    try:

        slot_price = driver.find_element_by_class_name('price-sec')
        print(f'Per Slot: {slot_price.text}')

    except:

        try:

            print(f'Per Slot: {item_price.text}')

        except Exception:

            pass

    # trader = driver.find_element_by_class_name('item-card')
    # print(trader)

    img_processing.log_image(result)
