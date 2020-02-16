from doc_processor import DocProcessor
from docx import Document
from docx.opc.exceptions import PackageNotFoundError 
from csv_creator import CsvCreator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.service import Service, ServiceTask, ServicePart
from models.base import Base
from pprint import pprint
import os

if __name__ == "__main__":    
    # Create engine
    # db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
    # engine = create_engine(db_uri, echo=True)#     
    db = create_engine('sqlite:///data.db', convert_unicode=True)
    # Base.metadata.create_all(bind=engine)

    filename = os.getenv('CSV_NAME')
    docs_folder = os.getenv('DOCS_FOLDER')    
        
    files = os.listdir(docs_folder)

    counter = 1
    budget_counter = 0

    documents = []

    for filename in files:            
        if counter > 3:
            break

        try:
            doc = Document('{}{}'.format(docs_folder, filename))
        except PackageNotFoundError as error:
            print('erro no arquivo {}'.format(filename))
            continue
        
        doc_processor = DocProcessor(doc)
        data = doc_processor.extract_data()
        plate = data['license_plate']
        phone1, phone2 = data['phone_numbers']
        is_budget = data['is_budget']

        if plate != 'CAMPO_VAZIO':
            if is_budget == 1:
                budget_counter = budget_counter + 1
                # print(filename)

            pprint(len(data['tables']))
            pprint(data['tables'])

            documents.append({
                "vehicle_name": "",
                "vehicle_number": "",
                "phone1": "",
                "phone2": "",
                "customer": data['customer'],
                "date": data['date'],
                "is_budget": str(is_budget),
                "tables": data['tables']
            })
            counter = counter + 1

            break


    # print(documents[0].get('tables'))

    # file_document = open(filename, 'w')
    # csv_creator = CsvCreator(filename, documents)
    # print('creating the csv with the data.')
    # csv_creator.create()
    # print('csv created!')    


    Session = sessionmaker(bind=db)
    session = Session()
    print(session)
    session.close()
    # users = session.query(User).order_by(User.id)
    # for user in users:
    #     print(user.username)
    # user1 = User(username='user1', password='12345')
    # user2 = User(username='user2', password='54321')
    # session.add(user1)
    # session.add(user2)
    # session.commit()
