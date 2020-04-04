from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import img_processing
import time
import os

if not os.path.exists('images'):
    os.makedirs('images')

driver = webdriver.Firefox()
driver.get("https://tarkov-market.com/tag/keys")
print('Ready')

def main():
    global driver
    
    search_bar = driver.find_element_by_css_selector("input[placeholder='Search'")
    #print('got search bar')
    search_bar.clear()
    #print(img_processing.run())
    search_bar.send_keys(img_processing.run())
    time.sleep(2.5)
    
    try:
        key_price = driver.find_element_by_class_name('price-main')
        print(key_price.text)
    except:
        print('No price detected')
    #driver.close()
