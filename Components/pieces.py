from .position import Position

class Piece(object):
    def __init__(self, color, name, x, y):
        self.color = color
        self.name = name
        self.position = Position(x, y)
        self.moves = []

    def __str__(self):
        return str(self.color[0] + self.name[0])

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

    def generateMoves(self, board, moves, num):
        """
        Piece Board String Numbers -> [List-of Positions]
        generates a list of positions, which are moves that a piece can make
        """
        lst_of_pos = []

        x = self.getPosition().getX()
        y = self.getPosition().getY()

        if 'pawn' in moves:
            if self.getColor() in 'white':
                # move forward 1
                if isinstance(board.getSquare(x, y - 1).getPiece(), str):
                    lst_of_pos.append(Position(x, y - 1))
                    # initial two-square advance
                    if y == 6 and isinstance(board.getSquare(x, y - 2).getPiece(), str):
                        lst_of_pos.append(Position(x, y - 2))
                
                # attack piece up left
                if isinstance(board.getSquare(x - 1, y - 1).getPiece(), Piece):
                    lst_of_pos.append(Position(x - 1, y - 1))
                
                # attack piece up right
                if isinstance(board.getSquare(x + 1, y - 1).getPiece(), Piece):
                    lst_of_pos.append(Position(x + 1, y - 1))
            
            else:
                # move up 1 square
                if isinstance(board.getSquare(x, y + 1).getPiece(), str):
                    lst_of_pos.append(Position(x, y + 1))
                    # initial 2 square advance
                    if y == 1 and isinstance(board.getSquare(x, y + 2).getPiece(), str):
                        lst_of_pos.append(Position(x, y + 2))
                
                # attack piece up left
                if isinstance(board.getSquare(x - 1, y + 1).getPiece(), Piece):
                    lst_of_pos.append(Position(x - 1, y + 1))
                
                # attack piece up right
                if isinstance(board.getSquare(x + 1, y + 1).getPiece(), Piece):
                    lst_of_pos.append(Position(x + 1, y + 1))

        if 'knight' in moves:
            # down 1 right 3
            if (x + 3 <= 7) and (y + 1 <= 7):
                if isinstance(board.getSquare(x + 3, y + 1).getPiece(), str):
                    lst_of_pos.append(Position(x + 3, y + 1))
                elif self.getColor() != board.getSquare(x + 3, y + 1).getPiece().getColor():
                    lst_of_pos.append(Position(x + 3, y + 1))
            # up 1 right 3
            if (x + 3 <= 7) and (y - 1 >= 0):
                if isinstance(board.getSquare(x + 3, y - 1).getPiece(), str):
                    lst_of_pos.append(Position(x + 3, y - 1))
                elif self.getColor() != board.getSquare(x + 3, y - 1).getPiece().getColor():
                    lst_of_pos.append(Position(x + 3, y - 1))
            # down 1 left 3
            if (x - 3 >= 0) and (y + 1 <= 7):
                if isinstance(board.getSquare(x - 3, y + 1).getPiece(), str):
                    lst_of_pos.append(Position(x - 3, y + 1))
                elif self.getColor() != board.getSquare(x - 3, y + 1).getPiece().getColor():
                    lst_of_pos.append(Position(x - 3, y + 1))
            # up 1 left 3
            if (x - 3 >= 0) and (y - 1 >= 0):
                if isinstance(board.getSquare(x - 3, y - 1).getPiece(), str):
                    lst_of_pos.append(Position(x - 3, y - 1))
                elif self.getColor() != board.getSquare(x - 3, y - 1).getPiece().getColor():
                    lst_of_pos.append(Position(x - 3, y - 1))
            # down 3 right 1
            if (x + 1 <= 7) and (y + 3 <= 7):
                if isinstance(board.getSquare(x + 1, y + 3).getPiece(), str):
                    lst_of_pos.append(Position(x + 1, y + 3))
                elif self.getColor() != board.getSquare(x + 1, y + 3).getPiece().getColor():
                    lst_of_pos.append(Position(x + 1, y + 3))
            # up 3 right 1
            if (x + 1 <= 7) and (y - 3 >= 0):
                if isinstance(board.getSquare(x + 1, y - 3).getPiece(), str):
                    lst_of_pos.append(Position(x + 1, y - 3))
                elif self.getColor() != board.getSquare(x + 1, y - 3).getPiece().getColor():
                    lst_of_pos.append(Position(x + 1, y - 3))
            # down 3 left 1
            if (x - 1 >= 0) and (y + 3 <= 7):
                if isinstance(board.getSquare(x - 1, y + 3).getPiece(), str):
                    lst_of_pos.append(Position(x - 1, y + 3))
                elif self.getColor() != board.getSquare(x - 1, y + 3).getPiece().getColor():
                    lst_of_pos.append(Position(x - 1, y + 3))
            # up 3 left 1
            if (x - 1 >= 0) and (y - 3 >= 0):
                if isinstance(board.getSquare(x - 1, y - 3).getPiece(), str):
                    lst_of_pos.append(Position(x - 1, y - 3))
                elif self.getColor() != board.getSquare(x - 1, y - 3).getPiece().getColor():
                    lst_of_pos.append(Position(x - 1, y - 3))
        
        else: 
            if 'up' in moves:
                for val in range(1, num + 1):
                    if y - val >= 0:
                        square = board.getSquare(x, y - val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x, y - val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x, y - val))
                        break
            
            if 'down' in moves:
                for val in range(1, num + 1):
                    if y + val <= 7:
                        square = board.getSquare(x, y + val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x, y + val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x, y + val))
                        break
            
            if 'left' in moves:
                for val in range(1, num + 1):
                    if x - val >= 0:
                        square = board.getSquare(x - val, y)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x - val, y))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x - val, y))
                        break
            
            if 'right' in moves:
                for val in range(1, num + 1):
                    if x + val <= 7:
                        square = board.getSquare(x + val, y)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x + val, y))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x + val, y))
                        break
            
            if 'up-left' in moves:
                for val in range(1, num + 1):
                    if x - val >= 0 and y - val >= 0:
                        square = board.getSquare(x - val, y - val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x - val, y - val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x - val, y - val))
                        break
            
            if 'down-left' in moves:
                for val in range(1, num + 1):
                    if x + val <= 7 and y - val >= 0:
                        square = board.getSquare(x + val, y - val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x + val, y - val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x + val, y - val))
                        break
            
            if 'up-right' in moves:
                for val in range(1, num + 1):
                    if x - val >= 0 and y + val <= 7:
                        square = board.getSquare(x - val, y + val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x - val, y + val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x - val, y + val))
                        break
            
            if 'down-right' in moves:
                for val in range(1, num + 1):
                    if x + val <= 7 and y + val <= 7:
                        square = board.getSquare(x + val, y + val)
                        if isinstance(square.getPiece(), str):
                            lst_of_pos.append(Position(x + val, y + val))
                            continue
                        elif square.getPiece().getColor() != self.getColor():
                            lst_of_pos.append(Position(x + val, y + val))
                        break

        return lst_of_pos
 
class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'king', x, y)

    def generateMoves(self, board):
        """
        King Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'up down left right up-left up-right down-left down-right', 1)

class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'queen', x, y)

    def generateNewMoves(self, board):
        """
        Queen Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'up down left, right up-left up-right down-left down-right', 7)

class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'bishop', x, y)

    def generateNewMoves(self, board):
        """
        Bishop Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'up-left up-right down-left down-right', 7)
            
class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'knight', x, y)

    def __str__(self):
        return str(self.color[0] + self.name[1])

    def generateNewMoves(self, board):
        """
        King Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'knight', 1)

class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'rook', x, y)

    def generateNewMoves(self, board):
        """
        King Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'up down left right', 7)

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, 'pawn', x, y)

    def generateNewMoves(self, board):
        """
        Pawn Board -> [List-of Positons]

        generates a list of positions that self can move to.
        """
        return super().generateMoves(board, 'pawn', 1)