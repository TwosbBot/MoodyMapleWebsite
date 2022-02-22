from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# todo 该用utf8还是utf8mb4?

address = "mysql+pymysql://root:wangxuhui123.0@localhost/Moodymaple?charset=utf8mb4"
engine = create_engine(address)

# proxy module
Session = sessionmaker(bind=engine,
                       autoflush=False,
                       autocommit=False
                       )

# https://stackoverflow.com/questions/21793590/pycharm-sqlalchemy-autocomplete
session = scoped_session(Session)
""":type: sqlalchemy.orm.Session"""

Base = declarative_base()
""":type: sqlalchemy.orm.DeclarativeMeta"""
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
    pass
