from .position import Position
from .piece import Piece

class Square(object):
    def __init__(self, x, y):
        self.piece = "--"
        self.position = Position(x, y)

    def __str__(self):
        if isinstance(self.piece, Piece):
            return self.piece.__str__()
        return self.piece
    
    def getPiece(self):
        return self.piece
    
    def setPiece(self, piece):
        self.piece = piece
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, newPosition):
        self.position = newPosition

    def addPiece(self, color, piece_name):
        """
            Square String String -> [Mutates self.piece]
        """
        self.setPiece(Piece(color, piece_name))

    def removePiece(self):
        """
            Square -> [Mutates self.piece]
        """
        self.setPiece('--')