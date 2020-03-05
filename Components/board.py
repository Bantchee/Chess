from .position import Position
from .pieces import *

class Board(object):
    columns = "abcdefgh"
    rows = "12345678"

    def __init__(self):
        self.board = []
        self.white_captured_pieces = []
        self.black_captured_pieces = []

        self.resetBoard()

    def getBoard(self):
        return self.board
    def getCapturedPieces(self, player):
        if player == 'white':
            return self.white_captured_pieces
        else:
            return self.black_captured_pieces
    def addCapturedPiece(self, player, piece):
        if player == 'white':
            self.getCapturedPieces(player).append(piece)
        else:
            self.getCapturedPieces(player).append(piece)
    def removeCapturedPiece(self, player, piece):
        if player == 'white':
            self.getCapturedPieces(player).remove(piece)
        else:
            self.getCapturedPieces(player).remove(piece)
    def getSquare(self, x, y):
        return self.board[y][x]

    def resetBoard(self):
        """
        -> [Mutates self.board]
        resest the board.
        """
        self.board = []
        
        for y in range(8):
            lst = []
            for x in range(8):
                lst.append(Square(x, y))
            self.getBoard().append(lst)

        # White
        self.getSquare(0, 7).setPiece(Rook("white", 0, 7))
        self.getSquare(1, 7).setPiece(Knight("white", 1, 7))
        self.getSquare(2, 7).setPiece(Bishop("white", 2, 7))
        self.getSquare(3, 7).setPiece(King("white",  3, 7))
        self.getSquare(4, 7).setPiece(Queen("white", 4, 7))
        self.getSquare(5, 7).setPiece(Bishop("white", 5, 7))
        self.getSquare(6, 7).setPiece(Knight("white", 6, 7))
        self.getSquare(7, 7).setPiece(Rook("white", 7, 7))
        self.getSquare(0, 6).setPiece(Pawn("white", 0, 6))
        self.getSquare(1, 6).setPiece(Pawn("white", 1, 6))
        self.getSquare(2, 6).setPiece(Pawn("white", 2, 6))
        self.getSquare(3, 6).setPiece(Pawn("white", 3, 6))
        self.getSquare(4, 6).setPiece(Pawn("white", 4, 6))
        self.getSquare(5, 6).setPiece(Pawn("white", 5, 6))
        self.getSquare(6, 6).setPiece(Pawn("white", 6, 6))
        self.getSquare(7, 6).setPiece(Pawn("white", 7, 6))

        # Black
        self.getSquare(0, 0).setPiece(Rook("black", 0, 0))
        self.getSquare(1, 0).setPiece(Knight("black", 1, 0))
        self.getSquare(2, 0).setPiece(Bishop("black", 2, 0))
        self.getSquare(3, 0).setPiece(King("black", 3, 0))
        self.getSquare(4, 0).setPiece(Queen("black", 4, 0))
        self.getSquare(5, 0).setPiece(Bishop("black", 5, 0))
        self.getSquare(6, 0).setPiece(Knight("black", 6, 0))
        self.getSquare(7, 0).setPiece(Rook("black", 7, 0))
        self.getSquare(0, 1).setPiece(Pawn("black", 0, 1))
        self.getSquare(1, 1).setPiece(Pawn("black", 1, 1))
        self.getSquare(2, 1).setPiece(Pawn("black", 2, 1))
        self.getSquare(3, 1).setPiece(Pawn("black", 3, 1))
        self.getSquare(4, 1).setPiece(Pawn("black", 4, 1))
        self.getSquare(5, 1).setPiece(Pawn("black", 5, 1))
        self.getSquare(6, 1).setPiece(Pawn("black", 6, 1))
        self.getSquare(7, 1).setPiece(Pawn("black", 7, 1))
        
    def pieceAtSquare(self, str_pos):
        """Board String -> Boolean
        if str_pos is less than 3 characters,
        if 1 character in str_pos is in [1, 2, 3, 4, 5, 6, 7, 8],
        if other character in str_pos is in [a, b, c, d, e, f, g, h],
        and if there is a piece at that location
        then return True
        """
        if len(str_pos) < 3:
            
            if (str_pos[0] in self.columns) or (str_pos[0] in self.rows):
                
                if (str_pos[1] in self.columns) or (str_pos[1] in self.rows):
                    pos = self.getPositionOfSquare(str_pos)
            
                    if isinstance(self.board[pos.getY()][pos.getX()].getPiece(), Piece):
                        temp_piece = self.board[pos.getY()][pos.getX()].getPiece()
                        
                        temp_piece.setMoves(temp_piece.generateNewMoves())

                        print("Piece", temp_piece, "at [" + str(pos.getX()), str(pos.getY()) + "]")
                        print("Possible moves: ", end = "")
                        for move in temp_piece.getMoves():
                            print(self.columns[move.getX()] + self.rows[move.getY()] + " ", end = "")
                        print()

                        return True
                else:
                    # print("Index 1 of", str_pos, "is not in", self.columns, "or", self.rows)
                    return False
            else:
                # print("Index 0 of", str_pos, "is not in", self.columns, "or", self.rows)
                return False               
        else:
            # print(str_pos, "is bigger than 3 characters")
            return False

    def possibleMove(self, origin, destination):
        """Board String String -> Boolean, Return true if destination is a possible move for Piece at origin"""
        if len(destination) < 3:
            
            if (destination[0] in self.columns) or (destination[0] in self.rows):
                
                if (destination[1] in self.columns) or (destination[1] in self.rows):
                    org_pos = self.getPositionOfSquare(origin)
                    des_pos = self.getPositionOfSquare(destination)
                    
                    if des_pos.isPositionInList(self.getBoard()[org_pos.getY()][org_pos.getX()].getPiece().getMoves()):
                        
                        if isinstance(self.getBoard()[des_pos.getY()][des_pos.getX()].getPiece(), Piece):
                            
                            if self.getBoard()[des_pos.getY()][des_pos.getX()].getPiece().getColor() == \
                               self.getBoard()[org_pos.getY()][org_pos.getX()].getPiece().getColor():
                                # print("You already have a piece at that location")
                                return False
                            
                            else:
                                return True
                        
                        else:
                            return True
                    
                    else:
                        # print("Piece can't move there")
                        return False
        
                else:
                    # print("Index 1 of destination,", destination, ", is not in", self.columns, "or", self.rows)
                    return False
            else:
                # print("Index 0 of destination,", destination, ", is not in", self.columns, "or", self.rows)
                return False
        else:
            # print("destination,", destination, ", is bigger than 3 characters")
            return False

    # Needs a method that checks str_pos
    # example input = wp, output = false
    def getPositionOfSquare(self, str_pos):
            """
            String -> Position

            return Square object at that position in board
            """
            if str_pos[0] in self.columns:
                position = Position(self.columns.index(str_pos[0]), self.rows.index(str_pos[1]))
                return position
            else:
                position = Position(self.columns.index(str_pos[1]), self.rows.index(str_pos[0]))
                return position

    def movePiece(self, player, origin, destination):
        """
            String Position Position -> [Mutates self.Board]
        """
        piece = self.board[origin.getY()][origin.getX()].getPiece()
        piece.setPosition(destination.getX(), destination.getY())

        if isinstance(self.board[destination.getY()][destination.getX()], Piece):
            self.addCapturedPiece(player, board[destination.getY()][destination.getX()].getPiece().__str__())
            self.board[destination.getY()][destination.getX()].setPiece(piece)
            self.board[origin.getY()][origin.getX()].setPiece("--")
        else:
            self.board[destination.getY()][destination.getX()].setPiece(piece)
            self.board[origin.getY()][origin.getX()].setPiece("--")

class Square(object):
    def __init__(self, x, y):
        self.piece = "--"
        self.position = Position(x, y)
    def getPiece(self):
        return self.piece
    def setPiece(self, piece):
        self.piece = piece
    def getPosition(self):
        return self.position
    def setPosition(self, newPosition):
        self.position = newPosition
    def __str__(self):
        if isinstance(self.piece, Piece):
            return self.piece.__str__()
        return self.piece