# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey

from db import db


class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(150))
    total = db.Column(db.Float(precision=2))
    # plate = Column(String)

    def __init__(self):
        self.id = ''
        self.customer = ''
        self.email = ''
        self.phone = ''
        self.total = ''
        self.license_plate = ''

    @classmethod
    def find_by_customer(cls, customer, plate):
        return cls.query\
                .filter_by(customer=customer)\
                .filter_by(plate=plate) #.first()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
