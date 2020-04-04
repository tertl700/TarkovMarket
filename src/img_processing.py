try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def run():
    key_text = ocr_core('images/key.png')
    if "EXAMINE: " in key_text:
        print(key_text.replace('EXAMINE: ', ''))
        return(key_text.replace('EXAMINE: ', ''))
    else:
        print('Not a key')
        return('Not a key')
#print(ocr_core('images/test.png'))