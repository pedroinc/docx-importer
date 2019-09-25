from doc_processor import DocProcessor
from csv_creator import CsvCreator
from docx import Document
import os


if __name__ == "__main__":    
    filename = os.getenv('CSV_NAME')
    docs_folder = os.getenv('DOCS_FOLDER')    
    
    csv_creator = CsvCreator(filename, docs_folder)
    csv_creator.create()