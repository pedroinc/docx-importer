from doc_processor import DocProcessor
from docx import Document
import unicodedata, os
from itertools import chain
from pprint import pprint

if __name__ == "__main__":
    # DocConverter().convert_docs_to_docx('docs', 'docx')   
    docs_folder = '/home/placerda/Downloads/pessoal/docs_ofi/all_docx/'
    
    try:
        # base_path = os.getcwd()
        files = os.listdir(docs_folder)
        counter = 0

        for filename in files:
            pprint('{} : {}'.format(counter, filename))
            counter = counter + 1
            # break

            # doc = Document('{}filename'.format(docs_folder))
            # doc_processor = DocProcessor(doc)

            # data = doc_processor.extract_data()
            # table_itens = chain(data['table_itens'])    

            # service_itens = [{ 
            #                     "id": int(item['ITEM']), 
            #                     "description": item['DESCRIÇÃO DO SERVIÇOS'],
            #                     "price": float(item['PREÇO']
            #                                 .replace('.', '')
            #                                 .replace(',', '.')) 
            #                                 if item['PREÇO'].strip() != ''  
            #                                 else '',
            #                 }
            #                 # it
            #                 for item in table_itens 
            #                 if 'DESCRIÇÃO DO SERVIÇOS' in item]

            # parts_itens = [item for item in table_itens]

            # pprint(service_itens)
            # pprint(parts_itens)

    except Exception as e:
        pprint(e)