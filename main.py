from doc_file import DocFile

if __name__ == "__main__":
    # DocFileHandler().convert_docs_to_docx('docs', 'docx')
    file = DocFile('docx/AII 8224 01.06.2010.docx')
    print(file.read_license_plate())
    # print(match)
    # read_tables(doc)






