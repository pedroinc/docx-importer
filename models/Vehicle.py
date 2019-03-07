from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    license_plate = Column(String)
    chassis_number = Column(String)

    # brand_id = Column(ForeignKey('brand.id'))
    # model_id = Column(ForeignKey('model.id'))
    # customer_id = Column(ForeignKey('customer.id'))
