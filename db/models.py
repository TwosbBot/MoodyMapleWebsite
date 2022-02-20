from sqlalchemy import Table, ForeignKey, Text, Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship



# String 对应varchar,
# Text对应tinytext? 文档里只写了text,先试试行不行的通吧

from .database import Base

# 本分的sqlalchemy不会额外定义default和has_null什么的

class UserInfo(Base):
    __tablename__ = "user_info"
    # Column 貌似是一个适配器
    qq = Column(String(10))
    account = Column(String(16), primary_key=True)

    # 可选
    def __repr__(self):
        return f"<UserInfo(qq={self.qq}, account={self.account}>"


# [一个账户和一个server]是唯一的,所以作为主键
#
class UserBundle(Base):
    __tablename__ = "user_bundle"

    server = Column(String(8), nullable=False, primary_key=True)
    account = Column(String(16),
                     ForeignKey("user_info.account"),
                     nullable=False,
                     primary_key=True,
                     )
    last_update_time = Column(DateTime,nullable=True)
    comment=Column(Text, nullable=False)

    # 貌似和生成表没有关系, 只是为了方便跨表查询
    pass

user_info = relationship("UserInfo", back_populates="user_bundle")