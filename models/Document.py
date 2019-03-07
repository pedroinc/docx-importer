from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    total = Column(String)
    license_plate = Column(String)

