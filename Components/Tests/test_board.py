import unittest
from .. import board
from .. import position
from .. import pieces

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.brd = board.Board()
    
    def tearDown(self):
       pass

    def test_resetBoard(self):
        self.brd.resetBoard()

        for col in self.brd.getBoard():
            for square in col:
                # black pieces
                if square.getPosition().getY() == 0:
                     # king
                    if square.getPosition().getX() == 3:
                        self.assertEqual(square.getPiece().__str__(), 'bk')
                    # queen
                    elif square.getPosition().getX() == 4:
                        self.assertEqual(square.getPiece().__str__(), 'bq')
                    # bishops
                    elif square.getPosition().getX() == 2 or square.getPosition().getX() == 5:
                        self.assertEqual(square.getPiece().__str__(), 'bb')
                    # knights
                    elif square.getPosition().getX() == 1 or square.getPosition().getX() == 6:
                        self.assertEqual(square.getPiece().__str__(), 'bn')
                    # rooks
                    elif square.getPosition().getX() == 0 or square.getPosition().getX() == 7:
                        self.assertEqual(square.getPiece().__str__(), 'br')
                elif square.getPosition().getY() == 1:
                    # pawns
                    self.assertEqual(square.getPiece().__str__(), 'bp')
                # white pieces
                elif square.getPosition().getY() == 6:
                    # pawns
                    self.assertEqual(square.getPiece().__str__(), 'wp')
                elif square.getPosition().getY() == 7:
                    # king
                    if square.getPosition().getX() == 3:
                        self.assertEqual(square.getPiece().__str__(), 'wk')
                    # queen
                    elif square.getPosition().getX() == 4:
                        self.assertEqual(square.getPiece().__str__(), 'wq')
                    # bishops
                    elif square.getPosition().getX() == 2 or square.getPosition().getX() == 5:
                        self.assertEqual(square.getPiece().__str__(), 'wb')
                    # knights
                    elif square.getPosition().getX() == 1 or square.getPosition().getX() == 6:
                        self.assertEqual(square.getPiece().__str__(), 'wn')
                    # rooks
                    elif square.getPosition().getX() == 0 or square.getPosition().getX() == 7:
                        self.assertEqual(square.getPiece().__str__(), 'wr')
                # empty square
                else:
                    self.assertEqual(square.getPiece(), '--')
    
    def test_pieceAtSquare(self):
        self.assertFalse(self.brd.pieceAtSquare('ae2'))
        self.assertFalse(self.brd.pieceAtSquare('j2'))
        self.assertFalse(self.brd.pieceAtSquare('a9'))
        self.assertTrue(self.brd.pieceAtSquare('b8'))
        self.assertTrue(self.brd.pieceAtSquare('2f'))
        self.assertFalse(self.brd.pieceAtSquare('g4'))
    
    def test_possibleMove(self):
        self.assertFalse(self.brd.possibleMove('a2', 'ae3'))
        self.assertFalse(self.brd.possibleMove('a2', 'j2'))
        self.assertFalse(self.brd.possibleMove('a2', 'a9'))
        self.assertTrue(self.brd.possibleMove('a2', '3a'))
        self.assertTrue(self.brd.possibleMove('7e', 'e6'))
        self.assertFalse(self.brd.possibleMove('b2', 'c6'))
    
    def test_getPositionOfSquare(self):
        self.assertEqual(self.brd.getPositionOfSquare('a2').__str__(), '[0, 1]')
        self.assertEqual(self.brd.getPositionOfSquare('d5').__str__(), '[3, 4]')
        self.assertEqual(self.brd.getPositionOfSquare('7h').__str__(), '[7, 6]')


    def test_movePiece(self):
        # pawn
        self.brd.movePiece('black', position.Position(1, 1), position.Position(0, 2))
        self.assertIsInstance(self.brd.getSquare(0, 2).getPiece(), pieces.Pawn)

        self.brd.movePiece('black', position.Position(0, 2), position.Position(0, 3))
        self.assertIsInstance(self.brd.getSquare(0, 3).getPiece(), pieces.Pawn)

        self.brd.movePiece('white', position.Position(0, 3), position.Position(1, 4))
        self.assertIsInstance(self.brd.getSquare(1, 4).getPiece(), pieces.Pawn)

if __name__ == '__main__':
        unittest.main()