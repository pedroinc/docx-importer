from csv_creator import CsvCreator
from sqlalchemy import create_engine
import os

from models.user import User
from models.service import Service, ServiceTask, ServicePart


if __name__ == "__main__":
    engine = create_engine('sqlite:///data.db', convert_unicode=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(username='placerda', password='12345')
    user2 = User(username='zelacerda', password='224455')

    print(session)

    session.add(user1)
    session.add(user2)

    session.commit()
    session.close()



    # filename = os.getenv('CSV_NAME')
    # docs_folder = os.getenv('DOCS_FOLDER')    
    
    # csv_creator = CsvCreator(filename, docs_folder)
    # print('creating the csv with the data.')
    # csv_creator.create()
    # print('csv created!')