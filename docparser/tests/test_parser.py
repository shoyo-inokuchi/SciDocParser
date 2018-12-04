import os
import unittest
from docparser.parser import parser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(unittest.TestCase):
    def setUp(self):
        print(BASE_DIR)
        #pdf_path =
        pass


class ParserTests(Base):
    def test_process_documents(self):
        pass

    def test_pdf_to_image(self):
        pass

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
