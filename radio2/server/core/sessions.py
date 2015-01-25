'''
Created on Jan 24, 2015

@author: dnash
'''

from sqlalchemy.orm import scoped_session, sessionmaker

session = scoped_session(sessionmaker())