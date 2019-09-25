from sqlalchemy import create_engine, Column, BigInteger, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import CurrencyType, Currency

Base = declarative_base()


class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True)
    is_estimate = Column(Boolean)
    vehicle = Column(String)
    chassis = Column(String)
    plate = Column(String)
    customer = Column(String)
    address = Column(String)
    phone1 = Column(String)
    phone2 = Column(String)
    date = Column(String)
    others = Column(String)
    total = Column(CurrencyType)


class ServiceTask(Base):
    __tablename__ = 'service_item'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    price = Column(CurrencyType)
    document_id = Column(ForeignKey('service.id'))


class ServicePart(Base):
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True)
    description = Column(String)    
    price_genuine = Column(CurrencyType)
    price_other = Column(CurrencyType)
    document_id = Column(ForeignKey('service.id'))


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


# engine = create_engine('sqlite:///data.db', echo=True)
engine = create_engine('sqlite:///data.db', convert_unicode=True)

Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(obj)
# session.commit()
# session.close()