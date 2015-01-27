'''
Created on Jan 25, 2015

@author: dashnash
'''
import unittest
from radio2.server.core import connect

from radio2.server.data import Base, Session
from radio2.server.core.models import Device, User, Command
from sqlalchemy.schema import CreateSchema, DropSchema

test_config_path = 'configs/unittests.json'

connection = connect.Connection(test_config_path)

class Test(unittest.TestCase):
    
#     def setUp(self):
#         connection = connect.Connection(test_config_path)
#         connection.engine.execute(DropSchema('unittests'))
#         connection.engine.execute(CreateSchema('unittests'))
# 
#         Session.configure(bind=connection.engine)        
#         Base.metadata.create_all(connection.engine)

    @classmethod
    def setUpClass(cls):
        Session.configure(bind=connection.engine)
        connection.engine.execute(DropSchema('unittests'))
        connection.engine.execute(CreateSchema('unittests'))
        Base.metadata.create_all(connection.engine)
        super(Test, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
    
    
#     def testAAASchemaCreate(self):
#         Base.metadata.create_all(connection.engine)
      
    def testDevicesAddandDelete(self):
#         connection = connect.Connection(test_config_path)
#         Session.configure(bind=connection.engine)
        test_session = Session()
        test_session.add_all([ \
            Device(name='dev1'), \
            Device(name='dev2'), \
            Device(name='dev3')])
        
        test_session.commit()
        
    def testCommandAddandDelete(self):
#         connection = connect.Connection(test_config_path)
#         Session.configure(bind=connection.engine)
        test_session = Session()
        
        dev = Device(name='testLinkDevice')
        usr = User(display_name='FunkyFresh', device_id='x10422_junk')
        comm = Command(op='Play pandora station \'Funk\'', user=usr, device=dev)
        
        test_session.add(comm)
        
        test_session.commit()
        
        self.assertTrue(len(usr.commands) == 1)
        self.assertTrue(comm.device == dev)
        
        
        
        
            
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSchemaCreate']
    unittest.main()