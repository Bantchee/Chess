import unittest
from .. import position

class TestPosition(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """runs once at the start"""
        pass
    
    @classmethod
    def tearDownClass(cls):
        """runs once at the end"""
        pass
    
    def setUp(self):
        """runs code before every single test"""
        self.pos_1 = position.Position(0, 0)
        self.pos_2 = position.Position(2, 3)
        self.pos_3 = position.Position(1, -5)
        
        self.list_of_pos = [self.pos_1, self.pos_3]
    
    def tearDown(self):
        print('tearDown\n')
        """runs code after every single test"""
        pass
        
    def test_isPositionInList(self):
        print('test_isPositionInList')
        self.assertTrue(self.pos_1.isPositionInList(self.list_of_pos))
        self.assertFalse(self.pos_2.isPositionInList(self.list_of_pos))
        self.assertTrue(self.pos_3.isPositionInList(self.list_of_pos))
        
if __name__ == '__main__':
    unittest.main()