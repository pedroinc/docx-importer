import re
from docx import Document
import subprocess
from doc_processor import DocProcessor
import os

class DocConverter:
    @staticmethod
    def convert_docs_to_docx(from_folder, to_folder):
        try:
            base_path = os.getcwd()
            files = os.listdir("{0}/{1}".format(base_path, from_folder))

            for filename in files:
                if filename.endswith('.doc'):
                    path_to_file = '{}/{}/{}'.format(
                        base_path, from_folder, filename)
                    subprocess.call(
                        ['soffice', '--headless', '--convert-to',
                        'docx', '--outdir', to_folder, path_to_file]
                    )
        except Exception as e:
            print(e)
