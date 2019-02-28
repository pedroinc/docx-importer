from docx import Document
import subprocess
import os
# import io

orig_folder = 'doc/'
dest_folder = 'docx/'


class DocHandler:

    def __init__(self):
        pass

    @staticmethod
    def convert_docs_to_docx():
        base_path = os.getcwd()
        origin_folder = os.listdir("{0}/{1}".format(os.getcwd(), orig_folder))
        print(orig_folder)
        # exit()

        for filename in origin_folder:
            if filename.endswith('.doc'):
                print(filename)
                # print('{0}{1}'.format(origin_folder, filename))

                subprocess.call(['soffice',
                                 '--headless',
                                 '--convert-to',
                                 'docx',
                                 '--outdir',
                                 'docx',
                                 '{}/doc/{}'.format(base_path, filename)])

    @staticmethod
    def read_docx(file_path):
        filename = 'docx/AJJ1198_25.09.2007.docx'
        f = open(filename, 'rb')
        document = Document(f)
        print(document.element)
        f.close()
        # with open(filename, 'rb') as f:
        #     source_stream = io.StringIO(f.read())
        #     document = Document(source_stream)
        #     print(document)
        #
        #     source_stream.close()


if __name__ == "__main__":
    # DocHandler().convert_docs_to_docx()
    DocHandler().read_docx('')

