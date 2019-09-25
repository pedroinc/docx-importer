from sqlalchemy import create_engine, Column, BigInteger, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import CurrencyType, Currency

Base = declarative_base()

class Document(Base):
    __tablename__ = 'document'

    id = Column(BigInteger, primary_key=True)
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


class ServiceItem(Base):
    __tablename__ = 'service_item'

    id = Column(BigInteger, primary_key=True)
    description = Column(String)
    price = Column(CurrencyType)
    document_id = Column(ForeignKey('document.id'))


class Part(Base):
    __tablename__ = 'part'

    id = Column(BigInteger, primary_key=True)
    description = Column(String)    
    price_genuine = Column(CurrencyType)
    price_other = Column(CurrencyType)
    document_id = Column(ForeignKey('document.id'))


engine = create_engine('sqlite:///data.db', echo=True)
Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(obj)
# session.commit()
# session.close()