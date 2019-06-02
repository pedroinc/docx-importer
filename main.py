from doc_processor import DocProcessor
from docx import Document
import re
import os

if __name__ == "__main__":

    try:
        # origin = '/home/placerda/Downloads/mecanica/docs'
        documents_path = '/home/placerda/Downloads/mecanica/all_docx'
        # DocProcessor().convert_docs_to_docx(origin, destin)

        my_documents = []
        from_folder = 'docx'
        
        base_path = os.getcwd()
        files = os.listdir(documents_path)
        i = 0
        for filename in files:
            if i >= 500:
                print("*************** {} itens".format(i))
                break

            # path_to_file = '{}/{}/{}'.format(base_path, from_folder, filename)
            # print(path_to_file)
            # print(filename)
            file = DocProcessor("{}/{}".format(documents_path, filename))
            # print(file.read_license_plate())
            if file.read_license_plate() or file.read_customer_name():
                print("{}, {}".format(file.read_license_plate(), file.read_customer_name()))

            # if file.read_date():
            #     print(file.read_date())
            # print(file.read_lines())    
            i = i + 1

    except Exception as e:
        print(e)
