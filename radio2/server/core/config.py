'''
Created on Jan 24, 2015

@author: dnash
'''

from os.path import exists
import json

CONFIG_KEYS = [u'CONNECT_STRING']

class Config(object):
    '''
    classdocs
    '''

    def __init__(self, config_path):
        '''
        Constructor
        '''
        
        if not exists(config_path):
            raise OSError('\'{0}\' is missing'.format(config_path))
        
        with open(config_path, 'r') as f:
            config_object = json.load(f)
            
        for key in CONFIG_KEYS:
            if key not in config_object.keys():
                raise ValueError('Missing config setting \'{0}\' in {1}'.format(key, config_path))
        
        self.SETTINGS = config_object