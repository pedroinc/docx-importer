import re
from enum import Enum
from datetime import datetime
from pprint import pprint
from itertools import chain


class RegexFieldTypes:
    #SERVICE_DATE = r'\d{2}.\d{2}.\d{4}'
    SERVICE_DATE = r'(DATA:)(.*)'       
    LICENSE_PLATE = r'(.*)([a-zA-Z]{3}\s\d{4})(.*)'
    VEHICLE_NAME = r'(CULO:)([a-zA-Z0-9. ][^#\r\n]{1,40})'
    PHONE = r'(TEL.:)(.*)([0-9/ ])'    
    CUSTOMER = r'(PROP.:)(.*)'    


class DocProcessor:    

    BUDGET_TAG = 'ORÇ'

    def __init__(self, docx_obj):
        self._docx = docx_obj

    @staticmethod
    def is_doc_budget(filename):
        return True if DocProcessor.BUDGET_TAG in filename else False;

    @staticmethod
    def set_nice_looking_keys(tuple_headers):
        new_keys = []
        for item in tuple_headers:
            if 'DESCRI' in item:
                new_keys.append('description')
            elif 'FAB' in item:
                new_keys.append('factory_code')
            elif 'GENU' in item:
                new_keys.append('genuine')                
            elif 'OUTRA' in item:
                new_keys.append('other')
            elif 'PRE' in item:
                new_keys.append('price') 
            else:
                new_keys.append(item.lower()) 
        return tuple(new_keys)

    def read_table_content(self):
        content_lines = []
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

                cool_keys = DocProcessor.set_nice_looking_keys(keys)
                row_data = dict(zip(cool_keys, text))
                
                pprint(row_data.get('description'))
                if row_data.get('description').strip() != '':
                    #service item
                    if 'price' in row_data:
                        str_price = row_data['price'].replace(',', '.') if ',' in row_data['price'] else row_data['price']

                        content_lines.append({ 
                            description: row_data.get('description'),
                            price: str_price
                        })
                    elif 'genuine' in row_data:
                        content_lines.append({
                            description: row_data.get('description'),
                            genuine: row_data['genuine'].replace(',', '.') if row_data['genuine'] else row_data['genuine'],
                            other: row_data['other'].replace(',', '.') if row_data['other'] else row_data['other'],
                        })
                    content_lines.append(row_data)
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
        pattern = RegexFieldTypes.PHONE  
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
                return ' '.join(match.group(match_group).strip().split())
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
        
    def extract_data(self):
        lines = self.read_lines()
        table_content = self.read_table_content()
        phones = self.read_phones(lines)

        #pprint(table_content)

        return {
            "license_plate" : DocProcessor.read_field(lines, RegexFieldTypes.LICENSE_PLATE, 2),
            "vehicle_name" : DocProcessor.read_field(lines, RegexFieldTypes.VEHICLE_NAME, 2),
            "phone_numbers" : phones,
            "customer" : DocProcessor.read_field(lines, RegexFieldTypes.CUSTOMER, 2),
            "date" : self.format_to_iso_date(DocProcessor.read_field(lines, RegexFieldTypes.SERVICE_DATE, 2)),
        }