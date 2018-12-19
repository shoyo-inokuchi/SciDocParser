import cv2
import pytesseract
from parse.process_doc import pdf_to_image

pdf_path = 'pdfs/test_single_word.pdf'
img = pdf_to_image(pdf_path)[0]
print(type(img))
h, w, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
print(boxes)

for b in boxes.splitlines():
    b = b.split(' ')
    if b[0].lower() == 'q':
        img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow(pdf_path, img)
cv2.waitKey(0)
