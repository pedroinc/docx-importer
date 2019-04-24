import re
from docx import Document
import subprocess
import os


class DocProcessor:

    LICENSE_PLATE_IN_DOC_PATTERN = "(.*)([a-zA-Z]{3}\s\d{4})(.*)$"

    LICENSE_PLATE_FILENAME_PATTERN = "([a-zA-Z]{3}\s\d{4})"


    def __init__(self, file_path):
        # super(DocFile, self).__init__()
        self._docx = Document(file_path)
        self._file_lines = self.read_lines()
        self.license_plate = self.read_license_plate()
        # self.phone_number, self.other_phone_number = self.match_phone_numbers()
        # self.customer_name = self.match_customer_name()

    # @staticmethod
    # def set_new_name():

    @staticmethod
    def normalize_names():
        pass

    @staticmethod
    def convert_docs_to_docx(from_folder, to_folder):
        try:
            base_path = os.getcwd()
            files = os.listdir("{0}/{1}".format(base_path, from_folder))

            for filename in files:
                if filename.endswith('.doc') and DocProcessor.file_name_valid(filename):
                    path_to_file = '{}/{}/{}'.format(base_path, from_folder, filename)
                    subprocess.call(
                        ['soffice', '--headless', '--convert-to',
                        'docx', '--outdir', to_folder, path_to_file]
                    )
        except Exception as e:
            print(e)

    @staticmethod
    def read_tables(self):
        for table in self._docx.tables:
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)

                # Establish the mapping based on the first row
                # headers; these will become the keys of our dictionary
                if i == 0:
                    keys = tuple(text)
                    continue

                # Construct a dictionary for this row, mapping
                # keys to values for this row
                row_data = dict(zip(keys, text))
                print(row_data)

    def read_lines(self):
        lines = []
        for line in self._docx.paragraphs:
            trimmed_text = line.text.strip()
            if trimmed_text != '':
                lines.append(trimmed_text)
        return lines

    @staticmethod
    def file_name_valid(filename):
        # print(filename)
        return re.match(DocProcessor.LICENSE_PLATE_FILENAME_PATTERN, filename)

    def read_license_plate(self):
        for line in self._file_lines:
            # print(line)
            match = re.match(DocProcessor.LICENSE_PLATE_IN_DOC_PATTERN, line)
            if match:
                return match.group(2)
        return None

    def read_customer_name(self):
        pass
