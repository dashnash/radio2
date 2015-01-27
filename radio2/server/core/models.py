'''
Created on Jan 26, 2015

@author: dashnash
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from radio2.server.data import Base

class Device(Base):
    '''
    Stores device information
    '''
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    commands = relationship("Command", backref=backref("device"))
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    device_id = Column(String(50))
    display_name = Column(String(50))
    commands = relationship("Command", backref=backref("user"))

class Command(Base):
    __tablename__ = 'commands'
    id = Column(Integer, primary_key=True)
    op = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    device_id = Column(Integer, ForeignKey('devices.id'))

class Station(Base):
    __tablename__ = 'stations'
    id = Column(Integer, primary_key=True)
    run_op = Column(String(255))
    run_op = Column(String(255))
    stop_op = Column(String(255))
    skip_op = Column(String(255))
    # TODO image? static url?
    
class ClientApp(Base):
    __tablename__ = 'client_apps'
    id = Column(Integer, primary_key=True)
    version_string = Column(String(10))
    get_url = Column(String(255))