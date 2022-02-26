from sqlalchemy import Text, UnicodeText, INT, VARCHAR, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class UserInfo(Base):
    __tablename__ = "user_info"
    # Column 貌似是一个适配器

    qq = Column(VARCHAR(10))
    account = Column(VARCHAR(16), primary_key=True)
    comment = Column(Text)

    def __init__(self, qq=None, account=None, comment=None):
        self.qq = qq
        self.account = account
        self.comment = comment
    # 可选

    def __repr__(self):
        return f"<UserInfo(qq={self.qq}, account={self.account}>"


# [一个账户和一个server]是唯一的,所以作为主键
#
class UserPlugin(Base):
    __tablename__ = "user_plugin"

    comment = Column("comment", Text(65536), nullable=True)  # tinytext
    server = Column("server", VARCHAR(8), nullable=False, primary_key=True)
    last_update_time = Column("last_update_time", DateTime, nullable=True)
    pack_id = Column("pack_id", INT, ForeignKey("plugin_info.pack_id",
                                                ondelete="CASCADE",
                                                onupdate="CASCADE",
                                                name="fk_pack_id2"),
                     nullable=False,
                     primary_key=True, )
    account = Column("account", VARCHAR(16),
                     ForeignKey("user_info.account",
                                ondelete="CASCADE",
                                onupdate="CASCADE",
                                name="fk_account"),
                     nullable=False,
                     primary_key=True,
                     )

    # 将此类本身链接到UserInfo(类名)类, back_populates用以确定另一方的连接的属性名.
    # 例如另一方定义的back_populates就是user_info.
    # back_populates是backref的"升级版"? https://zhuanlan.zhihu.com/p/66090718
    user_info = relationship("UserInfo", back_populates="user_plugin")
    plugin_info = relationship("PluginInfo", back_populates="user_plugin")

    def __init__(self, server: VARCHAR, account: VARCHAR, pack_id: INT,
                 last_update_time: DateTime = None, comment: Text = None):
        self.account = account
        self.server = server
        self.pack_id = pack_id
        self.last_update_time = last_update_time
        self.comment = comment


class PluginInfo(Base):
    __tablename__ = "plugin_info"

    pack_id = Column("pack_id", INT, nullable=False, autoincrement=True, primary_key=True)
    packname = Column("packname", Text(65536), nullable=False)
    developer = Column("developer", Text(65536), nullable=True)
    create_time = Column("create_time", DateTime, nullable=True)
    comment = Column("comment", UnicodeText, nullable=True)

    user_plugin = relationship("UserPlugin", order_by=UserPlugin.plugin_info, back_populates="user_plugin")

    def __init__(self, pack_id: INT, packname: Text,
                 developer: Text = None,
                 create_time: DateTime = None,
                 comment: UnicodeText = None):
        self.pack_id = pack_id
        self.packname = packname
        self.developer = developer
        self.create_time = create_time
        self.comment = comment


class FrameInfo(Base):
    __tablename__ = "frame_info"

    version = Column("version", VARCHAR(7), nullable=False, primary_key=True)
    comment = Column("comment", UnicodeText, nullable=True)
    filepath = Column("filepath", Text(65536), nullable=True)

    def __init__(self, version, comment=None, filepath=None):
        self.version = version
        self.comment = comment
        self.filepath = filepath


class PluginMD5(Base):
    __tablename__ = "plugin_md5"

    pack_id = Column("pack_id", INT,
                     ForeignKey("plugin_info.pack_id",
                                ondelete="CASCADE",
                                onupdate="CASCADE",
                                name="fk_pack_id1"),
                     nullable=False,
                     primary_key=True)
    pack_md5 = Column("pack_md5", VARCHAR(16), nullable=False, primary_key=True)
    version = Column("version", VARCHAR(10), nullable=True)
    comment = Column("comment", UnicodeText, nullable=True)
    frame_version = Column("frame_version", VARCHAR(7),
                           ForeignKey("frame_info.version",
                                      ondelete="CASCADE",
                                      onupdate="CASCADE",
                                      name="fk_frame_version"),
                           nullable=False)
    sys_depend = Column("sys_depend", VARCHAR(15), nullable=False)
    filepath = Column("filepath", Text(65536), nullable=True)
    update_time = Column("update_time", DateTime, nullable=True)

    frame_info = relationship("FrameInfo", order_by=FrameInfo.version, back_populates="plugin_md5")
    plugin_info = relationship("PluginInfo", order_by=PluginInfo.pack_id, back_populates="plugin_md5")


UserInfo.user_plugin = relationship("UserPlugin", order_by=UserPlugin.user_info, back_populates="user_info")

FrameInfo.plugin_md5 = relationship("PluginMD5", order_by=PluginMD5.frame_version, back_populates="frame_info")

PluginInfo.plugin_md5 = relationship("PluginMD5", order_by=PluginMD5.pack_id, back_populates="plugin_info")
