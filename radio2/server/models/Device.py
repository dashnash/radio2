'''
Created on Jan 24, 2015

@author: dnash
'''

from sqlalchemy import Column, Integer, String
from radio2.server.core import Base

class Device(Base):
    '''
    Stores device information
    '''
    __tablename__ = 'devices'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    test_field = Column(Integer)