'''
Created on Jan 24, 2015

@author: dnash
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base(
                        )
class Device(Base):
    '''
    Stores device information
    '''
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)