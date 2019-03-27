from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, Session

Base = declarative_base()


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    license_plate = Column(String(15))
    chassis_number = Column(String(150))
    # customer_id = Column(Integer, ForeignKey('customer.id'))

    # brand_id = Column(ForeignKey('brand.id'))
    # model_id = Column(ForeignKey('model.id'))
    # customer_id = Column(ForeignKey('customer.id'))


if __name__ == '__main__':
    db = create_engine('sqlite:///data.db')

    def setup_once(dburl, echo, num):
        "setup once.  create an engine, insert fixture data"
        global engine
        engine = create_engine(dburl, echo=echo)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        session = Session(engine)
        # sess.add_all([
        #     Parent(children=[Child() for j in range(100)])
        #     for i in range(num)
        # ])
        session.commit()
