'''
Created on Jan 24, 2015

@author: dnash
'''

from sqlalchemy import create_engine
from radio2.server.core.config import Config
class Connection(object):
    '''
    classdocs
    '''


    def __init__(self, config_path):
        '''
        Constructor
        '''
        self.config = Config(config_path)
        self.engine = create_engine(self.config.SETTINGS['CONNECT_STRING'])
        
        