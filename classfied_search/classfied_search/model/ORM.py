# -*- coding:utf8 -*-
from classfied_search.config import constants
import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    JSON,
    DateTime,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(constants.MYSQL_DEFINE)
DBsession = sessionmaker(bind=engine)
session = DBsession()
BaseModel = declarative_base()


class College_info(BaseModel):
    __tablename__ = 'all_info'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, default='')
    urlmd5 = Column(String, nullable=False, default='')
    info = Column(JSON, nullable=False, default={})
    create_time = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now)

    @classmethod
    def add(cls, college_info):
        record = cls(
            id=college_info.get('id'),
            url=college_info.get('url'),
            urlmd5=college_info.get('urlmd5'),
            info=college_info.get('info'),
            create_time=college_info.get('create_time'))
        session.add(record)
        session.flush()
        session.commit()
        return record

    @classmethod
    def query(cls, id):
        return session.query(College_info).filter_by(id=id).first()
