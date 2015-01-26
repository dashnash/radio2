'''
Created on Jan 25, 2015

@author: dashnash
'''
import unittest
from radio2.server.core import Session
from radio2.server.core import connect

test_config_path = 'configs/local_mysql.json'

class Test(unittest.TestCase):


    def testConnect(self):
        connection = connect.Connection(test_config_path)
        
        Session.configure(bind=connection.engine)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConnect']
    unittest.main()