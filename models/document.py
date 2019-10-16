from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import CurrencyType, Currency
from sqlalchemy import Column, BigInteger, String, Dec Float, Boolean, ForeignKey

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
    total = Column(String)

class ServiceItem(Base):
    __tablename__ = 'service_item'
    id = Column(BigInteger, primary_key=True)
    description = Column(String)
    price = Column(CurrencyType)
    document_id = Column(BigInteger, ForeignKey('document.id'))


class Part(Base):
    __tablename__ = 'part'
    id = Column(BigInteger, primary_key=True)
    description = Column(String)    
    price_genuine = Column(CurrencyType)
    price_other = Column(CurrencyType)
    document_id = Column(ForeignKey('document.id'))
