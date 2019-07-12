from doc_processor import DocProcessor
from docx import Document


if __name__ == "__main__":
    # DocConverter().convert_docs_to_docx('docs', 'docx')
   
    docs_folder = '/home/placerda/Downloads/pessoal/docs_ofi/all_docx/'
    doc = Document('{}AII 8224 01.06.2010.docx'.format(docs_folder))
    doc_processor = DocProcessor(doc)

    print(doc_processor.extract_data()['license_plate'])
    # print(match)
    # read_tables(doc)






