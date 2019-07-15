from doc_processor import DocProcessor
from docx import Document
import unicodedata, os
from itertools import chain
from pprint import pprint

if __name__ == "__main__":
    # DocConverter().convert_docs_to_docx('docs', 'docx')   
    docs_folder = '/home/placerda/Downloads/pessoal/docs_ofi/all_docx/'
    # try:
    #     base_path = os.getcwd()
    #     files = os.listdir("{0}/{1}".format(base_path, from_folder))

    #     for filename in files:
    #         pprint(filename)

    # Exception as e:
    #     pprint(e)    

    doc = Document('{}AII 8224 01.06.2010.docx'.format(docs_folder))
    doc_processor = DocProcessor(doc)

    data = doc_processor.extract_data()
    table_itens = chain(data['table_itens'])    

    service_itens = [{ 
                        "id": int(item['ITEM']), 
                        "description": item['DESCRIÇÃO DO SERVIÇOS'],
                        "price": float(item['PREÇO']
                                    .replace('.', '')
                                    .replace(',', '.')) 
                                    if item['PREÇO'].strip() != ''  
                                    else '',
                    }
                    # it
                    for item in table_itens 
                    if 'DESCRIÇÃO DO SERVIÇOS' in item]

    parts_itens = [item for item in table_itens]
    # parts_itens = [item for item in table_itens if 'GENUÍNA' in item]


pprint(service_itens)
pprint(parts_itens)
    # print(match)
    # read_tables(doc)






