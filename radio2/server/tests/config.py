'''
Created on Jan 24, 2015

@author: dnash
'''
import unittest

from radio2.server.core.config import Config, CONFIG_KEYS

test_config_path = 'configs/dev_rds.json'

class Test(unittest.TestCase):


    def test_loadConfig(self):
        config = Config(test_config_path)
        for config_key in CONFIG_KEYS:
            print '{0} - {1}'.format(config_key, config.SETTINGS[config_key])
            
        self.assertNotEqual(None, config)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()