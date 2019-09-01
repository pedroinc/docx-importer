from doc_processor import DocProcessor
from docx import Document
import os


if __name__ == "__main__":
        
    file_document = open('data.csv','w')

    docs_folder = '/home/placerda/Downloads/mecanica/all_docx/'
    files = os.listdir(docs_folder)
    file_document.write("LICENSE_PLATE, VEHICLE, PHONE_1, PHONE_2, CLIENT, SERVICE_DATE \n")

    counter = 1

    for filename in files:
        print(filename)
        if counter >= 1000:
            break        
        doc = Document('{}{}'.format(docs_folder, filename))
        doc_processor = DocProcessor(doc)

        data = doc_processor.extract_data()

        plate = data['license_plate']
        vehicle = data['vehicle_name']        
        phone1, phone2 = data['phone_numbers']
        customer = data['customer']
        date = data['date']

        file_document.write("{},{},{},{},{} \n".format(
            plate, 
            vehicle, 
            phone1,
            phone2,
            customer,
            date))
        
        counter = counter + 1

        # print(match)
        # read_tables(doc)






