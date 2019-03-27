from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db')

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    phone = Column(String(20))
    mobile = Column(String(20))
    email = Column(String(150))
    customer_id = Column(ForeignKey('customer.id'))
    vehicles = relationship("Vehicle")
