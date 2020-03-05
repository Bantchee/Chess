from .position import Position

class Piece(object):
    def __init__(self, color, name, x, y):
        self.color = color
        self.name = name
        self.position = Position(x, y)
        self.moves = []
    def getColor(self):
        return self.color
    def setColor(self, newColor):
        self.color = newColor
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName
    def getPosition(self):
        return self.position
    def setPosition(self, x, y):
        self.position = Position(x, y)
    def getMoves(self):
        return self.moves
    def setMoves(self, list_of_positions):
        self.moves = list_of_positions
    def __str__(self):
        return str(self.color[0] + self.name[0])
 
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'king', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        King -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []

        # Front
        if self.getPosition().getY() > 0:
            # Front Left
            if self.getPosition().getX() > 0:
                lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() - 1))

            lst.append(Position(self.getPosition().getX(), self.getPosition().getY() - 1))

            # Front Right
            if self.getPosition().getX() < 7:
                lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() - 1))

        # Right
        if self.getPosition().getX() < 7:
            lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY()))

        # Back
        if self.getPosition().getY() < 7:
            # Front Right
            if self.getPosition().getX() < 7:
                lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() + 1))
                
            lst.append(Position(self.getPosition().getX(), self.getPosition().getY() + 1))

            # Front Left
            if self.getPosition().getX() > 0:
                lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() + 1))

        # Left
        if self.getPosition().getX() > 0:
            lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY()))

        return lst

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'queen', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        Queen -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []
        
        for i in range(1, 8):
            # Front
            if self.getPosition().getY() - i >= 0:
                # Front Left
                if self.getPosition().getX() - i >= 0:
                    lst.append(Position(self.getPosition().getX() - i, self.getPosition().getY() - i))

                lst.append(Position(self.getPosition().getX(), self.getPosition().getY() - i))
    
                # Front Right
                if self.getPosition().getX() + i <= 7:
                    lst.append(Position(self.getPosition().getX() + i, self.getPosition().getY() - i))

            # Right
            if self.getPosition().getX() + i <= 7:
                lst.append(Position(self.getPosition().getX() + i, self.getPosition().getY()))

            # Back ------
            if self.getPosition().getY() + i <= 7:
                # Front Right
                if self.getPosition().getX() + i <= 7:
                    lst.append(Position(self.getPosition().getX() + i, self.getPosition().getY() + i))
                
                lst.append(Position(self.getPosition().getX(), self.getPosition().getY() + i))

                # Front Left
                if self.getPosition().getX() - i >= 0:
                    lst.append(Position(self.getPosition().getX() - i, self.getPosition().getY() + i))

            # Left
            if self.getPosition().getX() - i >= 0:
                lst.append(Position(self.getPosition().getX() - i, self.getPosition().getY()))

        return lst

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'bishop', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        Bishop -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []

        for value in range(1, 8):
            if self.getColor() == 'white':
                if (self.getPosition().getX() + value <= 7) and (self.getPosition().getY() + value <= 7):
                    lst.append(Position(self.getPosition().getX() + value, self.getPosition().getY() + value))
                
                if (self.getPosition().getX() - value >= 0) and (self.getPosition().getY() + value <= 7):
                    lst.append(Position(self.getPosition().getX() - value, self.getPosition().getY() + value))

                if (self.getPosition().getX() + value <= 7) and (self.getPosition().getY() - value >= 0):
                    lst.append(Position(self.getPosition().getX() + value, self.getPosition().getY() - value))

                if (self.getPosition().getX() - value >= 0) and (self.getPosition().getY() - value >= 0):
                    lst.append(Position(self.getPosition().getX() - value, self.getPosition().getY() - value))
            else: 
                if (self.getPosition().getX() + value <= 7) and (self.getPosition().getY() + value <= 7):
                    lst.append(Position(self.getPosition().getX() + value, self.getPosition().getY() + value))
                
                if (self.getPosition().getX() - value >= 0) and (self.getPosition().getY() + value <= 7):
                    lst.append(Position(self.getPosition().getX() - value, self.getPosition().getY() + value))

                if (self.getPosition().getX() + value <= 7) and (self.getPosition().getY() - value >= 0):
                    lst.append(Position(self.getPosition().getX() + value, self.getPosition().getY() - value))

                if (self.getPosition().getX() - value >= 0) and (self.getPosition().getY() - value >= 0):
                    lst.append(Position(self.getPosition().getX() - value, self.getPosition().getY() - value))

        return lst
            
class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'knight', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        King -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []

        if (self.getPosition().getX() + 3 <= 7) and (self.getPosition().getY() + 1 <= 7):
            lst.append(Position(self.getPosition().getX() + 3, self.getPosition().getY() + 1))
        
        if (self.getPosition().getX() + 3 <= 7) and (self.getPosition().getY() - 1 >= 0):
            lst.append(Position(self.getPosition().getX() + 3, self.getPosition().getY() - 1))
        
        if (self.getPosition().getX() - 3 >= 0) and (self.getPosition().getY() + 1 <= 7):
            lst.append(Position(self.getPosition().getX() - 3, self.getPosition().getY() + 1))
        
        if (self.getPosition().getX() - 3 >= 0) and (self.getPosition().getY() - 1 >= 0):
            lst.append(Position(self.getPosition().getX() - 3, self.getPosition().getY() - 1))
        
        if (self.getPosition().getX() + 1 <= 7) and (self.getPosition().getY() + 3 <= 7):
            lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() + 3))
        
        if (self.getPosition().getX() + 1 <= 7) and (self.getPosition().getY() - 3 >= 0):
            lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() - 3))
        
        if (self.getPosition().getX() - 1 >= 0) and (self.getPosition().getY() + 3 <= 7):
            lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() + 3))
        
        if (self.getPosition().getX() - 1 >= 0) and (self.getPosition().getY() - 3 >= 0):
            lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() - 3))

        return lst
    
    def __str__(self):
        return str(self.color[0] + self.name[1])

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'rook', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        King -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []

        for value in range(1, 8):
            if self.getColor() == 'white':
                if self.getPosition().getX() + value <= 7:
                    lst.append(Position( self.getPosition().getX() + value, self.getPosition().getY()))
                if self.getPosition().getX() - value >= 0:
                    lst.append(Position( self.getPosition().getX() - value, self.getPosition().getY()))
                if self.getPosition().getY() + value <= 7:
                    lst.append(Position( self.getPosition().getX(), self.getPosition().getY() + value))
                if self.getPosition().getY() - value >= 0:
                    lst.append(Position( self.getPosition().getX(), self.getPosition().getY() - value))
            else:
                if self.getPosition().getX() + value <= 7:
                    lst.append(Position( self.getPosition().getX() + value, self.getPosition().getY()))
                if self.getPosition().getX() - value >= 0:
                    lst.append(Position( self.getPosition().getX() - value, self.getPosition().getY()))
                if self.getPosition().getY() + value <= 7:
                    lst.append(Position( self.getPosition().getX(), self.getPosition().getY() + value))
                if self.getPosition().getY() - value >= 0:
                    lst.append(Position( self.getPosition().getX(), self.getPosition().getY() - value))
        
        return lst

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'pawn', x, y)
        self.setMoves(self.generateNewMoves())

    def generateNewMoves(self):
        """
        Pawn -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        lst = []
        
        if self.getColor() == "white":
            if self.getPosition().getY() < 7:
                if 0 < self.getPosition().getX():
                    lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() - 1))
                lst.append(Position(self.getPosition().getX(), self.getPosition().getY() - 1))
                if self.getPosition().getX() < 7:
                    lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() - 1))
        elif self.getColor() == 'black':
            if self.getPosition().getY() < 7:
                if 0 < self.getPosition().getX():
                    lst.append(Position(self.getPosition().getX() - 1, self.getPosition().getY() + 1))
                lst.append(Position(self.getPosition().getX(), self.getPosition().getY() + 1))
                if self.getPosition().getX() < 7:
                    lst.append(Position(self.getPosition().getX() + 1, self.getPosition().getY() + 1))

        return lst