import re
from enum import Enum

class RegexFieldTypes:
    #SERVICE_DATE = r'\d{2}.\d{2}.\d{4}'
    SERVICE_DATE = r'(DATA:)(.*)'       
    LICENSE_PLATE = r'(.*)([a-zA-Z]{3}\s\d{4})(.*)'
    VEHICLE_NAME = r'(CULO:)([a-zA-Z0-9. ]+)'
    PHONE = r'(TEL.:)(.*)([0-9]{4}.[0-9]{4})$'    
    CUSTOMER = r'(PROP.:)(.*)'

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
    def read_phones(lines):
        pattern = RegexFieldTypes.PHONE  
        for line in lines:
            match = re.match(pattern, line)
            if match:
                return match.group(2), match.group(3)
        return ''

    @staticmethod
    def read_field(lines, regex, match_group):
        for line in lines:
            match = re.search(regex, line)
            if match:
                return ' '.join(match.group(match_group).strip().split())
        return ''
        
    def extract_data(self):
        lines = self.read_lines()

        phones = DocProcessor.read_phones(lines)

        return {
            "license_plate" : DocProcessor.read_field(lines, RegexFieldTypes.LICENSE_PLATE, 2),
            "vehicle_name" : DocProcessor.read_field(lines, RegexFieldTypes.VEHICLE_NAME, 2),
            "phone_numbers" : phones,
            "customer" : DocProcessor.read_field(lines, RegexFieldTypes.CUSTOMER, 2),
            "date" : DocProcessor.read_field(lines, RegexFieldTypes.SERVICE_DATE, 2),
            #"tables": DocProcessor.read_table_content(self._docx.tables)
        }