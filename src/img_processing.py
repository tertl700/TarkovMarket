import glob
import os
import re

import cv2
import pytesseract
from PIL import Image, ImageOps

# load template image
template = cv2.imread('images/template.png', 0)


# match template to screenshot, identify where item text is and return top_left and bottom_right
def match(path):

    img = cv2.imread(path, 0)
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + 856, top_left[1] + 27)

    return top_left, bottom_right


# invert and resize image to improve OCR
def format_image(img):

    img = ImageOps.invert(img)
    basewidth = 1080
    wperc = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wperc)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    return img


# crop image to matched area, improve OCR by inverting and resizing image.
def crop(path):

    results = match(path)
    img = Image.open(path)
    top_left = results[0]
    bottom_right = results[1]
    cropped = img.crop((top_left[0]+29, top_left[1], bottom_right[0], bottom_right[1]))
    format_image(cropped)

    cropped.save('images/cropped.png')


# read text from image using OCR through tesseract
def ocr():

    crop('images/screenshot.png')
    text = pytesseract.image_to_string(Image.open('images/cropped.png'))
    print(f"raw text {text}")
    text = format_text(text)
    text = resolve_ocr_errors(text)
    return text


# format text to account for known OCR issues
def format_text(text):

    text = text.replace('@', '0')
    text = text.replace(',', ' ')
    text = text.replace('.', '')
    text = text.replace('(', ' ')
    text = text.replace(')', ' ')
    text = text.lstrip()

    return text


# resolve known OCR errors
# if list becomes unmanageable train tesseract with bender (Tarkov's font)
def resolve_ocr_errors(text):

    text = text.replace('180', '10')
    text = text.replace('FDE', '')
    text = text.replace('Seav', 'Scav')
    text = text.replace('32-round', '30-round')
    text = text.replace('[ex ia ele] jcer- ehe lela Wialz-lne mA NT}', 'Mosin bolt-action infantry rifle')
    ammo_regex = re.compile(r'[0-9]{3}[x][0-9]{2}')
    ammo_result = ammo_regex.search(text)

    if ammo_result is not None:

        result = ammo_result.group(0)
        text = text.replace(result, f'{result[:1]}.{result[1:]}')

    return text


# print and return text results from image
def run():

    text = ocr()
    print(chr(27) + "[2J")
    print(text)
    return text


# catalogue crops as working / broken for error logging
def log_image(result):

    if result:

        image_list = glob.glob('images/working_crop*.png')
        number_list = list()
        for i in image_list:
            number = i.replace('images\\working_crop', '')
            number = number.replace('.png', '')
            number_list.append(int(number))

        number = max(number_list) + 1
        os.rename('images/cropped.png', f'images/working_crop{number}.png')

    else:

        image_list = glob.glob('images/broken_crop*.png')
        number_list = list()
        for i in image_list:
            number = i.replace('images\\broken_crop', '')
            number = number.replace('.png', '')
            number_list.append(int(number))

        number = max(number_list)+1
        os.rename('images/cropped.png', f'images/broken_crop{number}.png')
