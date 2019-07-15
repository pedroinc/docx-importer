from doc_processor import DocProcessor
from docx import Document
from itertools import chain
from pprint import pprint
from logging import getLogger, basicConfig
import unicodedata
import locale
import os

logger = getLogger(__name__)
basicConfig(level='DEBUG')


if __name__ == "__main__":        
    docs_folder = '/home/placerda/Downloads/pessoal/docs_ofi/all_docx/'

    try:
        files = os.listdir(docs_folder)
        # counter = 0

        for filename in files:
            # pprint('{} : {}'.format(counter, filename))
            # counter = counter + 1

            doc = Document('{}{}'.format(docs_folder, filename))
            doc_processor = DocProcessor(doc)

            data = doc_processor.extract_data()
            table_itens = chain(data['table_itens'])    

            service_itens = [{ 
                                "id": int(item['ITEM']), 
                                "description": item['DESCRIÇÃO DO SERVIÇOS'],
                                "price": item['PREÇO']
                                            .replace('.', '')
                                            .replace(',', '.')
                                            if item['PREÇO'].strip() != ''  
                                            else '',
                            }
                            # it
                            for item in table_itens 
                            if item.get('DESCRIÇÃO DO SERVIÇOS')]

            parts_itens = [item for item in table_itens]

            pprint(doc_processor.extract_data()['license_plate'])

            # pprint(service_itens)
            # pprint(parts_itens)

    except Exception as e:
        logger.exception('oops')