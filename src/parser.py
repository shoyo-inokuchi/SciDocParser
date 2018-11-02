from PIL import Image
import pytesseract


def processDocumentImage(imagePath):
    # TODO: consider better file checking
    if not imagePath.lower().endswith('.png'):
        # convert to png
        pass
    
    doc_image = Image.open(imagePath)
    doc_text = pytesseract.image_to_string(doc_image)
    var2def, var2ref = naive_parse_vars(doc_text) 
    ret = redraw(doc_image, var2def, var2ref) 
    return ret


def naive_parse_vars(text):
    """ Naively parses document for variables defs and refs via template
    matching.
    :type text: str
    :rtype: tuple( dict(str, str), dict(str, list[int]) )
    """
    keyphrases = {
            "is denoted",
            ""
    }


path = '../pdfs/fourier.png'
processDocumentImage(path)

