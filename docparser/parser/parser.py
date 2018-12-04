import sys
from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2
import tempfile
import json

import time


def process_document(path):
    """
    Main, overarching parser function.
    Parses PDF document defined by path and returns processed data.
    :param str path: string of path to PDF document
    :return dict in JSON format for Javascript processing:
        dict['images'] ->   list of NumPy-array-images, an array per document
                            page
        dict['var2def'] ->  dictionary with vars mapped to sentence that
                            defined them
        dict['var2ref'] ->  dictionary with vars mapped to list of occurrence
                            coordinates
    """
    # TODO: consider more robust file checking
    if not path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    doc_images_rgb = pdf_to_image(path)
    doc_images_gray = [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) for image in doc_images_rgb]
    plaintxt = extract_image_text(doc_images_gray)
    var2def = extract_vars(plaintxt)
    var2ref = find_occurences(var2def, doc_images_gray)
    print(var2def)
    print(doc_images_rgb)
    return jsonify({'images': doc_images_rgb, 'var2def': var2def, 'var2ref': var2ref})


def pdf_to_image(pdf_path):
    """
    Takes in path for PDF document and returns corresponding image as a NumPy
    array, converting to a PIL Image object as an intermediate state.
    :param str pdf_path: directory path of PDF document
    :rtype np.array ret: images as a NumPy array of Numpy arrays (RGB)
    """
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdf_path, output_folder=path, fmt='jpg')
        if not images_from_path:
            print('Error converting path to jpg')
            sys.exit()
        np_images = []
        for image in images_from_path:
            np_images.append(np.array(image))
    return np_images


def extract_image_text(images):
    """
    Takes in document images as NumPy arrays and returns the contained text
    as a string.

    :param list[np.array] images: List of NumPy arrays for
    :rtype str ret: concatenated string of all text in PDF document
    """
    # TODO: be able to parse Greek symbols
    ret = ''
    for i in range(len(images)):
        doc_text = pytesseract.image_to_string(images[i])
        ret += doc_text
    return ret


def extract_vars(text):
    """
    (Naively) parses text for instances where variables are defined ("...x denotes...")
    and returns a dictionary where defined variables are mapped to the
    sentence that defines them.
        Ex. "x denotes number of people." would be mapped as
            {'x':'x denotes number of people.'}.

    :param str text: extracted document text
    :rtype dict[str, str] var2def: vars mapped to sentence that defined them
    """
    # TODO: handle documents where the same variable has multiple definitions.
    # TODO: map words to their specific definition, not the whole sentence.
    # TODO: add recognition for mutliple vars in a sentence, add more robust var recog

    keywords = keyword_set()
    var2def = {}

    text = text.replace('\n', ' ')
    for sentence in text.split('. '):
        var_candidate = None
        contains_keyword = False
        for word in sentence.split():
            if not var_candidate and len(word) == 1:
                var_candidate = word
            if not contains_keyword and word.lower() in keywords:
                contains_keyword = True
        if var_candidate and contains_keyword:
            var2def[var_candidate] = sentence

    return var2def


def keyword_set():
    words = {
        "denote"
        "denotes",
        "denoted",
        "represent"
        "represents",
        "represented",
        "means",
        "stands for",
        "let",
        "letting",
    }
    return words


def find_occurences(var2def, images):
    """
    For each variable in dictionary var2def, find all occurrences of that
    variable in each page of images. Return a dictionary where each
    variable is mapped to a List of ...

    :param PIL Image image:
    :param dict[str, str] var2def:
    :rtype ??? processed_image:
    :rtype
    """
    var2ref = {}
    for var in var2def:
        occurrences = template_match(letter_image[var], images)
        if occurrences is None:
            print(f'Expected {var} on image, got None.')
            sys.exit()
        var2ref[var] = occurrences
    return var2ref


def template_match(letter, images):
    ret = cv2.matchTemplate(letter, images)

    return ret


def jsonify(data):
    """
    Takes in processed data of document images and returns it in JSON format.
    :param dict data: dict object created in process_document() function
    :return: input data in JSON format
    """
    pass


if __name__ == '__main__':
    start = time.time()
    path = 'pdfs/test3.pdf'
    pd = process_document(path)
    end = time.time() - start
    print(f'Process took {end} s')
