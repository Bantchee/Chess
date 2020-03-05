import unittest
from .. import pieces
from .. import position

class TestPieces(unittest.TestCase):
	def setUp(self):
		self.king = pieces.King('black', 5, 5)
		self.queen = pieces.Queen('black', 5, 5)
		self.bishop = pieces.Bishop('black', 5, 5)
		self.knight = pieces.Knight('black', 5, 5)
		self.rook = pieces.Rook('black', 5, 5)
		self.pawn = pieces.Pawn('black', 5, 5)

	def tearDown(self):
		pass

	def test_generateNewMoves(self):
		self.king.generateNewMoves()
		self.assertTrue(self.king.getMoves())

		self.queen.generateNewMoves()
		self.assertTrue(self.queen.getMoves())

		self.bishop.generateNewMoves()
		self.assertTrue(self.bishop.getMoves())

		self.knight.generateNewMoves()
		self.assertTrue(self.knight.getMoves())

		self.rook.generateNewMoves()
		self.assertTrue(self.rook.getMoves())

		self.pawn.generateNewMoves()
		self.assertTrue(self.pawn.getMoves())

if __name__ == '__main__':
	unittest.main()