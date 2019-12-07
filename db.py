# from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# from models.user import User
# from models.service import Service, ServiceTask, ServicePart

Base = declarative_base()


# engine = create_engine('sqlite:///data.db', echo=True)

# engine = create_engine('sqlite:///data.db', convert_unicode=True)
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# user1 = User(username='placerda', password='12345')
# user2 = User(username='zelacerda', password='224455')

# print(session)

# session.add(user1)
# session.add(user2)

# session.commit()
# session.close()