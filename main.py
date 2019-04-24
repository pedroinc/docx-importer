from doc_processor import DocProcessor
from docx import Document
import re
import os

if __name__ == "__main__":

    try:

        # DocProcessor().convert_docs_to_docx('docs', 'docx')

        my_documents = []
        from_folder = 'docx'

        base_path = os.getcwd()
        files = os.listdir("{0}/{1}".format(base_path, from_folder))

        for filename in files:
            path_to_file = '{}/{}/{}'.format(base_path, from_folder, filename)
            # print(path_to_file)

            file = DocProcessor(path_to_file)
            print(file.read_customer_name())
            print(file.read_license_plate())

    except Exception as e:
        print(e)
