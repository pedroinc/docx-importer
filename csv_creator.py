from doc_processor import DocProcessor
from docx import Document
from docx.opc.exceptions import PackageNotFoundError 
import os

class CsvCreator:
    def __init__(self, filename, documents):
        self.filename = filename
        self.documents = documents       

    def create(self):                
        file_document = open(self.filename, 'w')
        
        file_columns = "LICENSE_PLATE, VEHICLE_NAME, VEHICLE_NUMBER, PHONE_1, PHONE_2, CLIENT, SERVICE_DATE, IS_BUDGET \n"""
        file_document.write(file_columns)

        for doc in documents:            
            # if counter > 100:
            #    break

            file_document.write("{},{},{},{},{},{},{} \n".format(
            doc.plate, 
            doc.vehicle_name,
            doc.vehicle_number,
            doc.phone1,
            doc.phone2,
            doc.customer,
            doc.date,
            doc.is_budget))