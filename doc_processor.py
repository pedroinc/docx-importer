import re
from docx import Document


class DocProcessor:
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

    def read_license_plate(self):
        pattern = "(.*)([a-zA-Z]{3}\s\d{4})(.*)$"
        for line in self._file_lines:
            # print(line)
            match = re.match(pattern, line)
            if match:
                return match.group(2)
        return ''

    def read_customer_name(self):
        pass

