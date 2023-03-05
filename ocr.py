import pytesseract
from PIL import Image

def run_ocr(image):
    return pytesseract.image_to_string(image)
