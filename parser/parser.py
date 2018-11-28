import sys
from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2
import tempfile


def process_document(path):
    # TODO: consider more robust file checking
    if not path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    doc_images = pdf_to_image(path)
    plaintxt = extract_image_text(doc_images)
    var2def = extract_vars(plaintxt)
    #var2ref =
    print(var2def)
    #return var2def, var2ref,


def pdf_to_image(pdf_path):
    """
    Takes in path for PDF document and returns corresponding image as a NumPy
    array, converting to a PIL Image object as an intermediate state.
    :param str pdf_path: directory path of PDF document
    :rtype np.array ret: image as a NumPy array
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


def keyword_set():
    words = {
        "denotes",
        "denoted",
        "represents",
        "represented",
        "means",
        "stands for",
        "let",
    }
    return words


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


def adf():
    var2ref = {}
    return var2ref


def find_occurences(letter, image):
    """

    :param PIL Image image:
    :param dict[str, str] var2def:
    :rtype ??? processed_image:
    :rtype
    """
    # cv2.matchTemplate(image, )
    pass


if __name__ == '__main__':
    path = 'pdfs/TeletrafficTheoryPresentationSubject.pdf'
    pd = process_document(path)
