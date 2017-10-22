# -*- coding: utf-8 -*-
"""视频存储"""
import datetime
import os
import yaml
from sqlalchemy import (
    Column,
    String,
    Integer,
    SmallInteger,
    DateTime,
)

current_dir = os.path.dirname(__file__)
params_path = os.path.join(current_dir, 'params.yaml')
"""存储数据库"""
# from spider.tools.db import make_session
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


def make_session(db_url):
    """根据数据库配置生成会话对象"""
    engine = create_engine(db_url)
    return sessionmaker(bind=engine)


# from spider.config.conf import params
from sqlalchemy.ext.declarative import declarative_base


def load_params():
    """解析params.yaml"""
    with open(params_path, 'r') as f:
        p = yaml.load(f)
        return p['params'][0]


params = load_params()

BaseModel = declarative_base()
DBSession = make_session(params['mysql_url'])


class Videos(BaseModel):
    __tablename__ = 'web_video'

    id = Column(Integer, primary_key=True)
    source = Column(String(10), nullable=False)
    task_id = Column(Integer, nullable=False)
    img_url = Column(String(200), nullable=False)
    duration = Column(Integer, nullable=False)
    title = Column(String(200), nullable=False)
    video_url = Column(String(200), nullable=False)
    video_url_md5 = Column(String(32), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)

    @classmethod
    def filter_exist(cls, videos):
        """将已经存在表中的数据滤除

        Args:
            videos (list<WebVideo>): video 下载链接
        Returns:
            list<WebVideo> 返回不存在的视频链接
        """
        if not videos:
            return []

        video_url_md5s = [x.video_url_md5 for x in videos]
        session = DBSession()
        query_result = session.query(cls.video_url_md5).\
            filter(cls.video_url_md5.in_(video_url_md5s)).all()
        session.commit()
        exist_urls = {x[0] for x in query_result}
        return [x for x in videos if x.video_url_md5 not in exist_urls]

    @classmethod
    def batch_add(cls, videos):
        """批量添加记录

        Args:
            videos (list<WebVideo>): video 下载链接
        """
        if not videos:
            return

        records = [cls(
            source=x.source,
            task_id=x.task_id,
            img_url=x.img_url,
            duration=x.duration,
            title=x.title,
            video_url=x.video_url,
            video_url_md5=x.video_url_md5,
        ) for x in videos]
        session = DBSession()
        session.add_all(records)
        session.flush()
        session.commit()
        return records


class DownloadInfo(BaseModel):
    __tablename__ = 'download_info'

    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, nullable=False)
    video_url = Column(String(200), nullable=False)
    video_title = Column(String(200), nullable=False)
    video_size = Column(Integer, nullable=False)
    status = Column(SmallInteger, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now)

    @classmethod
    def add(cls, video_info):
        """添加记录

        Args:
            video_info (VideoInfo): 格式信息
        """
        record = cls(
            video_id=video_info.video_id,
            video_url=video_info.video_url,
            video_title=video_info.title,
            video_size=video_info.size,
        )
        session = DBSession()
        session.add(record)
        session.flush()
        session.commit()
        return record

    @classmethod
    def update_status(cls, video_id, status=1):
        """添加记录

        Args:
            video_id (int): 视频id
            status (int): 1下载完成 0未下载
        """
        session = DBSession()
        target = session.query(cls).filter(cls.video_id == video_id)
        target.update({'status': status})
        session.commit()
