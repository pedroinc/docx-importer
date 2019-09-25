from doc_processor import DocProcessor
from docx import Document
import os

class CsvCreator:
    def __init__(self, filename, docs_folder):
        self.filename = filename
        self.docs_folder = docs_folder        

    def create(self):
        file_document = open(self.filename,'w')
        # docs_folder = '/home/placerda/Downloads/mecanica/all_docx/'
        files = os.listdir(self.docs_folder)
        file_document.write("LICENSE_PLATE, VEHICLE, PHONE_1, PHONE_2, CLIENT, SERVICE_DATE \n")

        counter = 1

        for filename in files:
            print(filename)
    #        if counter >= 3000:
    #            break        
            doc = Document('{}{}'.format(self.docs_folder, filename))
            doc_processor = DocProcessor(doc)

            data = doc_processor.extract_data()

            plate = data['license_plate']
            vehicle = data['vehicle_name']        
            phone1, phone2 = data['phone_numbers']
            customer = data['customer']
            date = data['date']

            if plate != 'CAMPO_VAZIO':
                file_document.write("{},{},{},{},{},{} \n".format(
                    plate, 
                    vehicle, 
                    phone1,
                    phone2,
                    customer,
                    date))

                counter = counter + 1