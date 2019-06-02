import unittest
from doc_processor import DocProcessor

class DocProcessorTest(unittest.TestCase):

    def setUp(self):
        self.processor = DocProcessor('docx/AJJ 1198 23.05.2008.docx')

    def test_read_date(self):
        # filename = 'AJJ 1198 23.05.2008.docx'
        assert self.processor.read_date() == '23/05/2008'

    def test_file_name_valid_if_match_license(self):
        assert self.processor.file_name_valid(' KMV 3966 ANYCAR.doc')

    def test_file_name_fails_if_cant_match_license(self):
        assert self.processor.file_name_valid('MARIA.doc') == None


if __name__ == '__main__':
    unittest.main()
