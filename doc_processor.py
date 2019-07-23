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
        index = 0
        for line in self._docx.paragraphs:            
            trimmed_text = line.text.strip()
            if trimmed_text != '' and index >= 3:
                lines.append(trimmed_text)
            index = index + 1
        return lines

    @staticmethod
    def read_vehicle_name(lines):
        pattern = "(CULO:)(.*\s)"
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2)
        return 'NOME_VEICULO'

    @staticmethod
    def read_license_plate(lines):
        pattern = "(.*)([a-zA-Z]{3}\s\d{4})(.*)$"
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2).strip()
        return ''

    @staticmethod
    def read_customer(lines):
        pattern = "(PROP.:)(.*)"
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2).strip()
        return ''

    @staticmethod
    def read_phone(lines):
        pattern = "(TEL.:)(.*\s)([0-9]{4} [0-9]{4})"        
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2), match.group(3)
        return ''        

    @staticmethod
    def read_date(lines):
        for line in lines:
            match = re.search(r'\d{2}.\d{2}.\d{4}$', line)
            if match:
                return match.group(0)
        return 'DATA_SERVICO'     

    def extract_data(self):
        lines = self.read_lines()

        return {
            "license_plate" : DocProcessor.read_license_plate(lines),
            "vehicle_name" : DocProcessor.read_vehicle_name(lines),
            "phone_numbers" : DocProcessor.read_phone(lines),
            "customer" : DocProcessor.read_customer(lines),
            "date" : DocProcessor.read_date(lines),
            #"tables": DocProcessor.read_table_content(self._docx.tables)
        }