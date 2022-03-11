import logging
import translators  # MIT License
import pytesseract  # APACHE 2.0 Licence


def ocr(img):
    # TODO put correct path to binary here or add tesseract to PATH
    # remove the line where tesseract_cmd is defined if you have it in your PATH
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # TODO install rus.traineddata from https://github.com/tesseract-ocr/tessdata/blob/main/rus.traineddata
        # copy file into Tesseract-OCR/tessdata
        return pytesseract.image_to_string(img, lang='rus')
    except Exception as e:
        logging.error(e)


def translate(text):
    return translators.deepl(query_text=text, from_language='ru', to_language='en')
