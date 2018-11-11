from pdf2image import convert_from_path
import tempfile

import pytesseract


def processDocument(path):
    # TODO: consider better file checking
    if not pdf_path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    ret = pdf_to_plaintext(path)


def pdf_to_plaintext(pdf_path):
    with tempfile.TemporaryDirectory() as path:
        doc_images = convert_from_path(pdf_path, output_folder=path, fmt='jpg')

    for i in range(len(doc_images)):
        doc_text = pytesseract.image_to_string(doc_images[i])
        print(doc_text)


def parse_vars(text):
    """ Naively parses document for variables defs and refs via template
    matching.
    :type text: str
    :rtype: tuple( dict(str, str), dict(str, list[int]) )
    """
    keywords = {
        "denotes",
        "represents",
        "means",
        "stands for",
    }

    var2def = {}
    
    for word in text:
        if word in keywords:
            pass


def redraw(image, var2def, var2ref):
    pass



if __name__ == '__main__':
    path = '../pdfs/fourier.pdf'
    processDocument(path)





