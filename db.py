# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = create_engine('sqlite:///data.db')



def setup_once(dburl, echo, num):
    "setup once.  create an engine, insert fixture data"
    global engine
    engine = create_engine(dburl, echo=echo)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # sess = Session(engine)
    # sess.add_all([
    #     Parent(children=[Child() for j in range(100)])
    #     for i in range(num)
    # ])
    sess.commit()
