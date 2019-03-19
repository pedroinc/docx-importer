from doc_processor import DocProcessor



if __name__ == "__main__":
    # DocFileHandler().convert_docs_to_docx('docs', 'docx')
    file = DocProcessor('docx/AII 8224 01.06.2010.docx')
    print(file.read_license_plate())
    # print(match)
    # read_tables(doc)






