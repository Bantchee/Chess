import unittest
from ..square import Square

class TestSquare(unittest.TestCase):
	def setUp(self):
		self.square = Square(0, 0)

	def test_addPiece(self):
		self.square.addPiece()

	def test_removePiece(self):
		pass