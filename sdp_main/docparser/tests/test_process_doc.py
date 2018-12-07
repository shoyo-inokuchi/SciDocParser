import unittest
from sdp_main.docparser.parse import process_doc as pd


class ParserTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_pdf_to_image(self):
        pdf_path = "pdfs/test_sample1.pdf"
        img = pd.pdf_to_image(pdf_path)
        images = pd.pdf_to_image(img)
        assert

    def test_extract_image_text(self):
        pass

    def test_find_occurrences(self):
        pass

    def test_template_match(self):
        pass

    def test_jsonify(self):
        pass


class ExtractVarsTests(Base):
    def test1(self):
        pass

    def test2(self):
        pass

    def test3(self):
        pass


if __name__ == '__main__':
    unittest.main()
