from pdf2image import convert_from_path
import tempfile
import pytesseract


def processDocument(path):
    # TODO: consider better file checking
    if not path.lower().endswith('.pdf'):
        raise Exception('File should be in PDF format')

    plaintxt = extract_PDFtext(path)
    var2def = extract_vars(plaintxt)



def extract_PDFtext(pdf_path):
    """
    Takes in path for PDF document and returns the text as a string.

    :param str pdf_path: directory path of PDF document
    :rtype str ret: concatenated string of all text in PDF document
    """
    with tempfile.TemporaryDirectory() as path:
        doc_images = convert_from_path(pdf_path, output_folder=path, fmt='jpg')

        ret = ''
        for i in range(len(doc_images)):
            doc_text = pytesseract.image_to_string(doc_images[i])
            ret += doc_text
        return ret


def extract_vars(text):
    """
    Parses text for instances where variables are defined ("...x denotes...")
    and returns a dictionary where defined variables are mapped to the
    sentence that defines them.
        Ex. "x denotes number of people." would be mapped as
            {'x':'x denotes number of people.'}.

    :param str text: extracted document text
    :rtype dict[str, str] var2def: vars mapped to sentence that defined them
    """
    # TODO: handle documents where the same variable has multiple definitions.
    # TODO: map words to their specific definition, not the whole sentence.
    keywords = {
        "denotes",
        "represents",
        "means",
        "stands for",
    }

    var2def = {}
    
    for sentence in text.split('.'):
        if :
            pass

    return var2def


def redraw(image, var2def, var2ref):
    pass



if __name__ == '__main__':
    path = '../pdfs/fourier.pdf'
    processDocument(path)

