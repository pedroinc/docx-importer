import re

class DocProcessor:
    def __init__(self, docx_obj):
        self._docx = docx_obj

    @staticmethod
    def read_table_content(doc_tables):
        content_lines = []
        for table in doc_tables:         
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
                content_lines.append(row_data)
                # print(row_data)
        return content_lines

    def read_lines(self):
        lines = []
        for line in self._docx.paragraphs:
            trimmed_text = line.text.strip()
            if trimmed_text != '':
                lines.append(trimmed_text)
        return lines

    @staticmethod
    def read_license_plate(lines):
        pattern = "(.*)([a-zA-Z]{3}\s\d{4})(.*)$"
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2)
        return ''

    def add_service_itens(self):
        pass

    def add_parts(self):
        pass

    def extract_data(self):
        lines = self.read_lines()        

        return {
            "license_plate" : DocProcessor.read_license_plate(lines),
            "table_itens": DocProcessor.read_table_content(self._docx.tables)
        }