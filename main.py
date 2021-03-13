from barcode import EAN13
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode
from PIL import Image
from pdf2image import convert_from_path
import cv2

def pdf_to_pic(pdf_path, pic_path, pic_type, pic_dpi=200):
    pages = convert_from_path(pdf_path, pic_dpi)
    for page in pages:
        page.save(pic_path, pic_type)

def generate_barcode(barcode_path, barcode_type, barcode_content):
    barcode_types = {
        'EAN13': EAN13
    }
    with open(barcode_path, 'wb') as f:
        barcode_types.get(barcode_type)(barcode_content, writer=ImageWriter()).write(f)

def decode_barcode(barcode_path):
    # image_read = Image.open(barcode_path)
    image_read = cv2.imread(barcode_path)
    for i in decode(image_read):
        print(i.data.decode("utf-8"))
    print(decode(image_read))

def identify_barcode(barcode_path):
    # image_read = Image.open(barcode_path)
    image_read = cv2.imread(barcode_path)
    result = decode(image_read)

    image_barcode_highlight = cv2.rectangle(img, (result[0].rect.left, result[0].rect.top), 
        (result[0].rect.left + result[0].rect.width, result[0].rect.top + result[0].rect.height),
        color=(0, 255, 0),
        thickness=5)

    cv2.imshow("img", image_barcode_highlight)
    cv2.waitKey(0)

if __name__ == '__main__':
    # identify_barcode('./files/out.png')
    # generate_barcode('./files/generated_barcode.png', 'EAN13', '123456789101')
    pdf_to_pic('./files/unimed_boleto-nov.pdf', './files/unimed_boleto-nov.png', 'PNG', 200)
    decode_barcode('./files/unimed_boleto-nov.png')

