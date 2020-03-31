from .position import *
from .pieces import *

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

    def addPiece(self, color, piece):
        if piece == 'king':
            self.piece = King(color, self.getPosition().getX(), self.getPosition().getY())
        elif piece == 'queen':
            self.piece = Queen(color, self.getPosition().getX(), self.getPosition().getY())
        elif piece == 'bishop':
            self.piece = Bishop(color, self.getPosition().getX(), self.getPosition().getY())
        elif piece == 'knight':
            self.piece = Knight(color, self.getPosition().getX(), self.getPosition().getY())
        elif piece == 'rook':
            self.piece = Rook(color, self.getPosition().getX(), self.getPosition().getY())
        elif piece == 'pawn':
            self.piece = Pawn(color, self.getPosition().getX(), self.getPosition().getY())

    def removePiece(self):
        self.setPiece == '--'