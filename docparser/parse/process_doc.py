import pdf2image
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
        dict['var2ref'] ->  dictionary with vars mapped to all occurrence
                            coordinates for each page
    """
    # TODO: consider more robust file checking
    if not path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    doc_images_rgb = pdf_to_image(path)
    # TODO: test whether this conversion actually saves time
    doc_images_gray = [cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                       for image
                       in doc_images_rgb]
    plaintxt = extract_image_text(doc_images_gray)
    var2def = extract_vars(plaintxt)
    var2ref = find_occurrences(var2def, doc_images_gray)
    return jsonify({'images': doc_images_rgb,
                    'var2def': var2def,
                    'var2ref': var2ref})


def pdf_to_image(pdf_path):
    """
    Takes in path for PDF document and returns corresponding image as a NumPy
    array, converting to a PIL Image object as an intermediate state.
    :param str pdf_path: directory path of PDF document
    :rtype List[np.array] ret: list of images as Numpy arrays (RGB)
    """
    with tempfile.TemporaryDirectory() as path:
        images_from_path = pdf2image.convert_from_path(pdf_path,
                                                       output_folder=path,
                                                       fmt='jpg')
        if not images_from_path:
            raise Exception('Could not convert path to jpg')
        np_images = []
        for image in images_from_path:
            np_images.append(np.array(image))
    return np_images


def extract_image_text(images):
    """
    Takes in document images as NumPy arrays and returns the contained text
    as a string.

    :param list[np.array] images: List of NumPy array images
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
    Parses text for instances where variables are defined ("...x denotes...")
    and returns a dictionary where defined variables are mapped to the sentence
    that defines them.
    Ex. "x denotes number of people." would be mapped as:
        {'x':'x denotes number of people.'}.

    :param str text: extracted document text
    :rtype dict[str, str] var2def: vars mapped to sentence that defined them
    """
    # TODO: add more robust var recognition
    # TODO: handle documents where the same variable has multiple definitions.
    # TODO: add recognition for multiple vars in a sentence
    # TODO: map words to their specific definition, not the whole sentence.

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


def find_occurrences(var2def, images):
    """
    For each variable in dictionary var2def, find all occurrences of that
    variable in each page of images.

    :param dict[str, str] var2def: dictionary of variables mapped to the
                                   sentence that defined it.
    :param List[np.array] images: list of images of each page in the document
    :rtype dict[str, list[list[tuple(tuple(int,int), tuple(int,int))]]] var2ref:
                dictionary where each variable is mapped to:
                    a list of sub-lists, where each sub-list denotes a single
                    page of the document.
                    each sub-list contains every coordinate where the a
                    variable occurs on the page.
                    each coordinate is denoted by 2 tuples, where the first
                    tuple denotes the top left coordinate, the second tuple
                    denotes the bottom right coordinate.
    """
    all_letters2coords = {}
    for image in images:
        h, w, _ = image.shape
        boxes = pytesseract.image_to_boxes(image)

        for b in boxes.splitlines():
            b = b.split()
            letter = b[0]
            top_left = (b[1], b[2])
            bot_right = (b[3], b[4])
            coords = (top_left, bot_right)
            if letter in all_letters2coords:
                all_letters2coords[letter].append(coords)
            else:
                all_letters2coords[letter] = [coords]

    var2ref = {}
    for var in var2def:
        var2ref[var] = all_letters2coords[var]
    return var2ref


def jsonify(data):
    """
    Takes in processed data of document images and returns it in JSON format.
    :param dict data: dictionary object created in process_document() function
    :return: data converted to JSON format
    """
    return data


if __name__ == '__main__':
    start = time.time()
    path = '../pdfs/test_single_word.pdf'
    pd = process_document(path)
    end = time.time() - start
    print(f'Process took {end} s')
