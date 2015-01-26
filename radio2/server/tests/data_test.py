'''
Created on Jan 25, 2015

@author: dashnash
'''
import unittest
from radio2.server.core import connect

from radio2.server.core import Base, Session
from radio2.server.models.Device import Device

test_config_path = 'configs/unittests.json'

class Test(unittest.TestCase):
    
    def testSchemaCreate(self):
        connection = connect.Connection(test_config_path)
        Base.metadata.create_all(connection.engine)
    
    def testDevicesAddandDelete(self):
        connection = connect.Connection(test_config_path)
        Session.configure(bind=connection.engine)
        test_session = Session()
        test_session.add_all([ \
            Device(name='dev1'), \
            Device(name='dev2'), \
            Device(name='dev3')])
        
        test_session.commit()
        
        
        
        
        
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSchemaCreate']
    unittest.main()