from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# todo 该用utf8还是utf8mb4?
import models

address = "mysql+pymysql://root:wangxuhui123.0@localhost/Moodymaple?charset=utf8mb4"
engine = create_engine(address)

# proxy module
Session = sessionmaker(bind=engine,
                       autoflush=False,
                       autocommit=False)

db_session = scoped_session(Session)

# 映射的基类
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

    pass


