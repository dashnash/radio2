'''
Created on Jan 26, 2015

@author: dashnash
'''
from sqlalchemy import Column, Integer, String
from radio2.server.data import Base

class Device(Base):
    '''
    Stores device information
    '''
    __tablename__ = 'devices'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    test_field = Column(Integer)

class Command(Base):
    __tablename__ = 'commands'
    id = Column(Integer, primary_key=True)
    op = Column(String(255))
    #TODO link to user
    #TODO link to device
    

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    run_op = Column(String(255))
    run_op = Column(String(255))
    stop_op = Column(String(255))
    skip_op = Column(String(255))
    # TODO image? static url?
    
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    device_id = Column(String(50))
    display_name = Column(String(50))
    
class ClientApps(Base):
    __tablename__ = 'client_apps'
    id = Column(Integer, primary_key=True)
    version_string = Column(String(10))
    get_url = Column(String(255))