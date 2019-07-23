from doc_processor import DocProcessor
from docx import Document
import os


if __name__ == "__main__":
        
    data_file = open('data.csv','w')

    docs_folder = '/home/placerda/Downloads/mecanica/all_docx/'
    files = os.listdir(docs_folder)
    counter = 1

    for filename in files:
        print(filename)
        if counter >= 100:
            break        

        doc = Document('{}{}'.format(docs_folder, filename))
        doc_processor = DocProcessor(doc)

        data = doc_processor.extract_data()

        plate = data['license_plate']
        vehicle = data['vehicle_name']
        phone_numbers = data['phone_numbers']
        customer = data['customer']
        date = data['date']

        data_file.write("{},{},{},{},{} \n".format(
            plate, 
            vehicle, 
            phone_numbers,
            customer,
            date))
        
        counter = counter + 1

        # print(match)
        # read_tables(doc)






