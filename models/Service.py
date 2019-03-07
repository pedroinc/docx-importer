from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    discount = Column(String)
    date = Column(String)
    total = Column(String)
    customer_id = Column(ForeignKey('customer.id'))
    vehicle_id = Column(ForeignKey('vehicle.id'))


class ServiceItem(Base):
    __tablename__ = 'service_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(String)
    service_id = Column(ForeignKey('service.id'))
