from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    mobile = Column(String)
    customer_id = Column(ForeignKey('customer.id'))
