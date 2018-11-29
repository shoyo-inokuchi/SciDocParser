import sys
import time
import cv2
import numpy as np
import tempfile
from pdf2image import convert_from_path


def template_match(images, letter, threshold=0.8):
    matches = {}
    for i in range(len(images)):
        res = cv2.matchTemplate(images[i], letter, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        print(loc)
        matches[i + 1] = loc
    return matches


def pdf2image(pdf_path):
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdf_path, output_folder=path, fmt='jpg')
        if not images_from_path:
            print('Error converting path to jpg')
            sys.exit()
        np_images = []
        for image in images_from_path:
            np_images.append(np.array(image))
    return [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in np_images]


def path2image(path):
    return cv2.imread(path, 0)


if __name__ == '__main__':
    pdf_path = 'pdfs/test1.pdf'
    letter_path = 'letters/s2.png'

    start = time.time()
    ret = template_match(pdf2image(pdf_path), path2image(letter_path))
    print(f'Process took {time.time() - start} s')
    print(ret)
