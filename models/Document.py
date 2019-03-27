from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String, Boolean, ForeignKey

Base = declarative_base()


class Document(Base):
    __tablename__ = 'documents'

    id = Column(BigInteger, primary_key=True)
    is_estimate = Column(Boolean)
    vehicle = Column(String)
    chassis = Column(String)
    plate = Column(String)
    customer = Column(String)
    address = Column(String)
    phone = Column(String)
    date = Column(String)
    others = Column(String)
    total = Column(String)

    def __init__(self):
        self.id = ''
        self.vehicle = ''
        self.chassis = ''
        self.plate = ''
        self.customer = ''
        self.address = ''
        self.phone = ''
        self.date = ''
        self.others = ''
        self.total = ''

    @classmethod
    def search(cls, customer, vehicle):
        return cls.query\
                .filter_by(customer=customer)\
                .filter_by(vehicle=vehicle) #.first()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()


class ServiceItem(Base):
    __tablename__ = 'service_items'
    id = Column(BigInteger, primary_key=True)
    description = Column(String)
    price = Column(String)
    service_id = Column(ForeignKey('service.id'))

    def __init__(self):
        self.id = ''
        self.description = ''
        self.price = ''
        self.total = ''


class Parts(Base):
    __tablename__ = 'parts'
    id = Column(BigInteger, primary_key=True)
    description = Column(String)
    price = Column(String)
    part_id = Column(ForeignKey('part.id'))
