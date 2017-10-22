# -*- coding:utf8 -*-
from minitask.core import constants
import datetime
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from collections import namedtuple

video_info = namedtuple('video_info',['id','pic','mov','description','plays','create_time','upper','duration','site_src'])

engine = create_engine(constants.MYSQL_DEFINE)
DBsession = sessionmaker(bind=engine)
session = DBsession()
BaseModel = declarative_base()

class Video_info(BaseModel):

    __tablename__ = 'video_info'

    id = Column(Integer, primary_key=True)
    pic = Column(String[255], nullable=False, default='')
    mov = Column(Integer, nullable=False, default=0)
    description = Column(String[255], nullable=False, default='')
    plays = Column(Integer, nullable=False, default=0)
    create_time = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now)
    upper = Column(String[255], nullable=False, default='')
    duration = Column(Integer, nullable=False, default=0)
    site_src = Column(String[255], nullable=False, default='')

    @classmethod
    def add(cls,video_info):
        record = cls(id=video_info.id,pic=video_info.pic,mov=video_info.mov,description=video_info.description,
                     plays=video_info.plays,create_time=video_info.create_time,upper=video_info.upper,
                     duration=video_info.duration,site_src=video_info.site_src)
        session.add(record)
        session.flush()
        session.commit()
        return record