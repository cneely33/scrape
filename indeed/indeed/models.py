from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import indeed.settings

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**indeed.settings.DATABASE))

DeclarativeBase = declarative_base()

def create_jobs_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    
class Jobs(DeclarativeBase):
    """Indeed Jobs Model"""
    __tablename__="policejobs"
    
    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    link = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    company = Column('company', String, nullable=True)
    #original_price = Column('original_price', String, nullable=True)
    #price = Column('price', String, nullable=True)
    #end_date = Column('end_date', DateTime, nullable=True)
        #import Datetime in sqlalchemy to use datetime