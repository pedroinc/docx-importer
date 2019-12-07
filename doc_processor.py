import os
import re
from docx import Document
from enum import Enum
from datetime import datetime

class FieldType:
    #SERVICE_DATE = r'\d{2}.\d{2}.\d{4}'
    SERVICE_DATE = r'(DATA:)(.*)'       
    LICENSE_PLATE = r'(.*)([a-zA-Z]{3}\s\d{4})(.*)'
    VEHICLE_NAME = r'(CULO:)([a-zA-Z0-9. ][^#\r\n]{1,40})'    
    
    # vin number: vehicle identification number (chassi)
    VEHICLE_NUMBER = r'(CHASSI:)([a-zA-Z0-9. ][^#\r\n]{1,18})'
    PHONE = r'(TEL.:)(.*)([0-9/ ])'    
    CUSTOMER = r'(PROP.:)(.*)'
    IS_BUDGET = 'ORÇAMENTO'

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

    def read_phones(self, lines):
        pattern = FieldType.PHONE  
        for line in lines:
            match = re.match(pattern, line)
            if match:
                phones = match.group(2).split('/')

                return self.format_phone(phones[0]), self.format_phone(phones[1]) if len(phones) > 1 else self.format_phone(phones[0])

        return 'CAMPO_VAZIO', 'CAMPO_VAZIO'

    @staticmethod
    def read_field(lines, regex, match_group):
        for line in lines:
            match = re.search(regex, line)
            if match:
                return ' '.join(match
                                .group(match_group)
                                .strip()
                                .split())
        return 'CAMPO_VAZIO'
        
    def format_phone(self, phone_string):
        return phone_string.strip().replace('(', '').replace(')', '').replace(' ', '')

    def format_to_iso_date(self, str_date):
        if str_date == 'CAMPO_VAZIO':
            return str_date

        str_date_hyphen = str_date.replace(' ', '').replace(',', '.').replace('.', '-')        
        try:
            date_object = datetime.strptime(str_date_hyphen, '%d-%m-%Y').date()

            return date_object.isoformat()
        except Exception as e:
            print(e)
            return 'ERRO'
        
    @staticmethod
    def is_budget(lines):
        for line in lines:
            if line.find(FieldType.IS_BUDGET):
                print(line)
                return 1
        return 0
            

    def extract_data(self):
        lines = self.read_lines()
        phones = self.read_phones(lines)

        return {
            "license_plate" : DocProcessor.read_field(lines, 
                                            FieldType.LICENSE_PLATE, 2),
            "vehicle_name" : DocProcessor.read_field(lines, 
                                            FieldType.VEHICLE_NAME, 2),
            "vehicle_number" : DocProcessor.read_field(lines, 
                                            FieldType.VEHICLE_NUMBER, 2),
            "phone_numbers" : phones,    

            "customer" : DocProcessor.read_field(lines, 
                                            FieldType.CUSTOMER, 2),
            "date" : self.format_to_iso_date(DocProcessor.read_field(lines, 
                                            FieldType.SERVICE_DATE, 2)),
            "is_budget" : DocProcessor.is_budget(lines),

            "tables": DocProcessor.read_table_content(self._docx.tables)
        }