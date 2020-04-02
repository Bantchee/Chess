from .position import Position

class Piece(object):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.moves = []

    def __str__(self):
        if self.name == 'knight':
            return str(self.color[0] + self.name[1])
        return str(self.color[0] + self.name[0])

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getMoves(self):
        return self.moves

    def setMoves(self, list_of_positions):
        self.moves = list_of_positions

    def generateMoves(self, square, board):
        """
        Piece Board String Numbers -> [List-of Positions]
        generates a list of positions, which are moves that a piece can make
        """
        if self.name == 'pawn':
            return self.generatePawnMoves(square, board)

        elif self.name == 'rook':
            return self.generateRookMoves(square, board)

        elif self.name == 'knight':
            return self.generateKnightMoves(square, board)

        elif self.name == 'bishop':
            return self.generateBishopMoves(square, board)

        elif self.name == 'queen':
            return self.generateQueenMoves(square, board)

        elif self.name == 'king':
            return self.generateKingMoves(square, board)

    def generatePawnMoves(self, square, board):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        if self.getColor() == 'white':
            if y - 1 >= 0:
                # move forward 1
                if isinstance(board.getSquare(x, y - 1).getPiece(), str):
                    lst_of_pos.append(Position(x, y - 1))
                    # initial two-square advance
                    if y == 6 and isinstance(board.getSquare(x, y - 2).getPiece(), str):
                        lst_of_pos.append(Position(x, y - 2))
                # attack piece up left
                if x - 1 >= 0:
                    if isinstance(board.getSquare(x - 1, y - 1).getPiece(), Piece):
                        lst_of_pos.append(Position(x - 1, y - 1))
                # attack piece up right
                if x + 1 <= 7:
                    if isinstance(board.getSquare(x + 1, y - 1).getPiece(), Piece):
                        lst_of_pos.append(Position(x + 1, y - 1))

        elif self.getColor() == 'black':
            if y + 1 <= 7:
                # move up 1 square
                if isinstance(board.getSquare(x, y + 1).getPiece(), str):
                    lst_of_pos.append(Position(x, y + 1))
                    # initial 2 square advance
                    if y == 1 and isinstance(board.getSquare(x, y + 2).getPiece(), str):
                        lst_of_pos.append(Position(x, y + 2))
                # attack piece up left
                if x - 1 >= 0:
                    if isinstance(board.getSquare(x - 1, y + 1).getPiece(), Piece):
                        lst_of_pos.append(Position(x - 1, y + 1))
                # attack piece up right
                if x + 1 <= 7:
                    if isinstance(board.getSquare(x + 1, y + 1).getPiece(), Piece):
                        lst_of_pos.append(Position(x + 1, y + 1))

        return lst_of_pos 

    def generateRookMoves(self, square, board):
        return self.generateUpMoves(square, board, 8) + self.generateDownMoves(square, board, 8) \
            + self.generateLeftMoves(square, board, 8) + self.generateRightMoves(square, board, 8)

    def generateKnightMoves(self, square, board):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

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

        return lst_of_pos

    def generateBishopMoves(self, square, board):
        return self.generateLeftUpMoves(square, board, 8) + self.generateRightUpMoves(square, board, 8) \
            + self.generateLeftDownMoves(square, board, 8) + self.generateRightDownMoves(square, board, 8)

    def generateQueenMoves(self, square, board):
        return self.generateLeftUpMoves(square, board, 8) + self.generateUpMoves(square, board, 8) \
            + self.generateRightUpMoves(square, board, 8) + self.generateRightMoves(square, board, 8) \
            + self.generateRightDownMoves(square, board, 8) + self.generateDownMoves(square, board, 8) \
            + self.generateLeftDownMoves(square, board, 8) + self.generateLeftMoves(square, board, 8)

        return lst_of_pos

    def generateKingMoves(self, square, board):
        return self.generateLeftUpMoves(square, board, 2) + self.generateUpMoves(square, board, 2) \
            + self.generateRightUpMoves(square, board, 2) + self.generateRightMoves(square, board, 2) \
            + self.generateRightDownMoves(square, board, 2) + self.generateDownMoves(square, board, 2) \
            + self.generateLeftDownMoves(square, board, 2) + self.generateLeftMoves(square, board, 2)

    def generateUpMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if y - val >= 0:
                square = board.getSquare(x, y - val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x, y - val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x, y - val))
                break

        return lst_of_pos

    def generateDownMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if y + val <= 7:
                square = board.getSquare(x, y + val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x, y + val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x, y + val))
                break

        return lst_of_pos

    def generateLeftMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x - val >= 0:
                square = board.getSquare(x - val, y)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x - val, y))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x - val, y))
                break

        return lst_of_pos

    def generateRightMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x + val <= 7:
                square = board.getSquare(x + val, y)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x + val, y))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x + val, y))
                break
        return lst_of_pos

    def generateLeftUpMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x - val >= 0 and y - val >= 0:
                square = board.getSquare(x - val, y - val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x - val, y - val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x - val, y - val))
                break
        return lst_of_pos

    def generateRightUpMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x + val <= 7 and y - val >= 0:
                square = board.getSquare(x + val, y - val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x + val, y - val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x + val, y - val))
                break
        return lst_of_pos

    def generateLeftDownMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x - val >= 0 and y + val <= 7:
                square = board.getSquare(x - val, y + val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x - val, y + val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x - val, y + val))
                break
        return lst_of_pos

    def generateRightDownMoves(self, square, board, number):
        lst_of_pos = []

        x = square.getPosition().getX()
        y = square.getPosition().getY()

        for val in range(1, number):
            if x + val <= 7 and y + val <= 7:
                square = board.getSquare(x + val, y + val)
                if isinstance(square.getPiece(), str):
                    lst_of_pos.append(Position(x + val, y + val))
                    continue
                elif square.getPiece().getColor() != self.getColor():
                    lst_of_pos.append(Position(x + val, y + val))
                break

        return lst_of_pos