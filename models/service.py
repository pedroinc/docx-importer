from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy_utils import CurrencyType, Currency
from sqlalchemy.ext.declarative import declarative_base
from models.base import Base

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    is_approved = Column(Boolean)
    vehicle = Column(String(255))
    chassis = Column(String(255))
    plate = Column(String(255))
    customer = Column(String(255))
    address = Column(String(255))
    phone1 = Column(String(255))
    phone2 = Column(String(255))
    date = Column(String(255))
    others = Column(String(1000))
    comments = Column(String(1000))
    total = Column(CurrencyType)
    tasks = relationship("ServiceTask")
    parts = relationship("ServicePart")


class ServiceTask(Base):
    __tablename__ = 'service_task'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    description = Column(String(1000))
    price = Column(CurrencyType)
    document_id = Column(Integer, ForeignKey('service.id'))


class ServicePart(Base):
    __tablename__ = 'service_part'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    description = Column(String(1000))
    code = Column(String(255))
    price_genuine = Column(CurrencyType)
    price_other = Column(CurrencyType)
    document_id = Column(Integer, ForeignKey('service.id'))