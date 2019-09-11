from doc_processor import DocProcessor
from docx import Document
import os

if __name__ == "__main__":
        
    try:
        f_services = open('services.csv','w')
        docs_folder = '/home/placerda/Downloads/mecanica/all_docx/'
        files = os.listdir(docs_folder)

        table_headers = "plate, vehicle, phone_1, phone_2, customer, service_date, is_budget  \n"
        f_services.write(table_headers)
        counter = 1

        for filename in files:
            # if 'lock.' in filename:
            #     continue

            #'LNJ 8432 28.05.2012'
            # if 'LNJ 8432 28' not in filename:
            #     continue
            if counter >= 2:
                break        
            doc = Document('{}{}'.format(docs_folder, filename))
            doc_processor = DocProcessor(doc)

            data = doc_processor.extract_data()

            plate = data['license_plate']
            vehicle = data['vehicle_name']        
            phone1, phone2 = data['phone_numbers']
            customer = data['customer']
            date = data['date']
            is_budget = DocProcessor.is_doc_budget(filename)

            if plate != 'CAMPO_VAZIO':
                f_services.write("{},{},{},{},{},{},{} \n".format(
                    plate, 
                    vehicle, 
                    phone1,
                    phone2,
                    customer,
                    date,
                    is_budget))
                counter = counter + 1
            # print(match)
            # read_tables(doc)

    except Exception as e:
        print(e)