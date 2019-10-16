from doc_processor import DocProcessor
from docx import Document
from docx.opc.exceptions import PackageNotFoundError 
import os

class CsvCreator:
    def __init__(self, filename, docs_folder):
        self.filename = filename
        self.docs_folder = docs_folder        

    def create(self):                
        file_document = open(self.filename,'w')
        files = os.listdir(self.docs_folder)

        file_columns = "LICENSE_PLATE, VEHICLE_NAME, VEHICLE_NUMBER, PHONE_1, PHONE_2, CLIENT, SERVICE_DATE, IS_BUDGET \n"""

        file_document.write(file_columns)

        counter = 1
        budget_counter = 0

        for filename in files:            
            if counter > 100:
               break

            try:
                doc = Document('{}{}'.format(self.docs_folder, filename))
            except PackageNotFoundError as error:
                print('erro no arquivo {}'.format(filename))
                continue
            
            doc_processor = DocProcessor(doc)

            data = doc_processor.extract_data()

            plate = data['license_plate']
            phone1, phone2 = data['phone_numbers']
            is_budget = data['is_budget']

            if plate != 'CAMPO_VAZIO':

                if is_budget == 1:
                    budget_counter = budget_counter + 1
                    print(filename)

                file_document.write("{},{},{},{},{},{},{} \n".format(
                    plate, 
                    data['vehicle_name'],
                    data['vehicle_number'],
                    phone1,
                    phone2,
                    data['customer'],
                    data['date'],
                    str(is_budget)))

                counter = counter + 1

        print(budget_counter)