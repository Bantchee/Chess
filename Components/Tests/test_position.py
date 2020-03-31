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

    def test_getX(self):
        self.assertEqual(self.pos_1.getX(), 0)
        self.assertEqual(self.pos_2.getX(), 2)
        self.assertEqual(self.pos_3.getX(), 1)
    
    def test_setX(self):
        self.pos_1.setX(3)
        self.assertEqual(self.pos_1.getX(), 3)
        self.pos_2.setX(-2)
        self.assertEqual(self.pos_2.getX(), -2)
        self.pos_3.setX(6)
        self.assertEqual(self.pos_3.getX(), 6)
    
    def test_getY(self):
        self.assertEqual(self.pos_1.getY(), 0)
        self.assertEqual(self.pos_2.getY(), 3)
        self.assertEqual(self.pos_3.getY(), -5)

    def test_setY(self):
        self.pos_1.setX(-3)
        self.assertEqual(self.pos_1.getX(), -3)
        self.pos_2.setX(0)
        self.assertEqual(self.pos_2.getX(), 0)
        self.pos_3.setX(4)
        self.assertEqual(self.pos_3.getX(), 4)
        
    def test_isPositionInList(self):
        print('test_isPositionInList')
        self.assertTrue(self.pos_1.isPositionInList(self.list_of_pos))
        self.assertFalse(self.pos_2.isPositionInList(self.list_of_pos))
        self.assertTrue(self.pos_3.isPositionInList(self.list_of_pos))
        
if __name__ == '__main__':
    unittest.main()