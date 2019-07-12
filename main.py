from doc_processor import DocProcessor
from docx import Document
import unicodedata
from itertools import chain

if __name__ == "__main__":
    # DocConverter().convert_docs_to_docx('docs', 'docx')
   
    docs_folder = '/home/placerda/Downloads/pessoal/docs_ofi/all_docx/'
    doc = Document('{}AII 8224 01.06.2010.docx'.format(docs_folder))
    doc_processor = DocProcessor(doc)

    data = doc_processor.extract_data()

    table_itens = chain(data['table_itens'])    

    itens_servicos = [
                        { "id": int(it['ITEM']) }
                        for it in table_itens 
                        if 'DESCRIÇÃO DO SERVIÇOS' in it]
    itens_pecas = [it for it in table_itens if 'GENUÍNA' in it]


    print(itens_servicos)

    # print(match)
    # read_tables(doc)






