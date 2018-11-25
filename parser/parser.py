import sys
from pdf2image import convert_from_path
import pytesseract
import cv2


def process_document(path):
    # TODO: consider more robust file checking
    if not path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    doc_images = pdf_to_jpg(path)
    plaintxt = extract_pdf_text(doc_images)
    var2def = extract_vars(plaintxt)
    print(var2def)


def pdf_to_jpg(pdf_path):
    """
    Takes in path for PDF document and returns corresponding Image object.
    :param str pdf_path: directory path of PDF document
    :rtype Image ret: Image object in jpg format
    """
    ret = convert_from_path(pdf_path, fmt='jpg')
    if not ret:
        print('Error converting path to jpg')
        sys.exit()
    return ret


def extract_pdf_text(images):
    """
    Takes in PIL Image object and returns the contained text as a string.

    :param str images: directory path of PDF document
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

    keywords = {
        "denotes",
        "represents",
        "means",
        "stands for",
        "let",
    }

    common_vars = {
        'x', 'y', 'z', 'a', 'b', 't'
    }

    var2def = {}

    text = text.replace('\n', ' ')
    for sentence in text.split('. '):
        var_candidate = None
        contains_keyword = False
        for word in sentence.split():
            if word in common_vars:
                var_candidate = word
            if word in keywords:
                contains_keyword = True
        if var_candidate and contains_keyword:
            var2def[var_candidate] = sentence

    return var2def


def redraw(image, var2def):
    """

    :param PIL Image image:
    :param dict[str, str] var2def:
    :rtype ??? processed_image:
    :rtype
    """
    cv2.matchTemplate(image, )


if __name__ == '__main__':
    path = 'pdfs/test1.pdf'
    pd = process_document(path)
