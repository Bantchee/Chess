from .position import Position
from .piece import Piece
from .square import Square

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
    
    def getCapturedPieces(self, color):
        if color == 'white':
            return self.white_captured_pieces
        else:
            return self.black_captured_pieces
    
    def addCapturedPiece(self, piece):
        if piece.getColor() == 'white':
            self.getCapturedPieces('white').append(piece.__str__())
        else:
            self.getCapturedPieces('black').append(piece.__str__())
    
    def removeCapturedPiece(self, player, piece):
        if player == 'white':
            self.getCapturedPieces(player).remove(piece)
        else:
            self.getCapturedPieces(player).remove(piece)
    
    def getSquare(self, x, y):
        return self.board[y][x]

    def resetBoard(self):
        """
        Board -> [Mutates self.board]
        
        resest the board.
        """
        self.board = []
        
        for y in range(8):
            lst = []
            for x in range(8):
                lst.append(Square(x, y))
            self.getBoard().append(lst)

        # White
        self.getSquare(0, 7).addPiece('white', 'rook')
        self.getSquare(1, 7).addPiece('white', 'knight')
        self.getSquare(2, 7).addPiece('white', 'bishop')
        self.getSquare(3, 7).addPiece('white', 'king')
        self.getSquare(4, 7).addPiece('white', 'queen')
        self.getSquare(5, 7).addPiece('white', 'bishop')
        self.getSquare(6, 7).addPiece('white', 'knight')
        self.getSquare(7, 7).addPiece('white', 'rook')
        self.getSquare(0, 6).addPiece('white', 'pawn')
        self.getSquare(1, 6).addPiece('white', 'pawn')
        self.getSquare(2, 6).addPiece('white', 'pawn')
        self.getSquare(3, 6).addPiece('white', 'pawn')
        self.getSquare(4, 6).addPiece('white', 'pawn')
        self.getSquare(5, 6).addPiece('white', 'pawn')
        self.getSquare(6, 6).addPiece('white', 'pawn')
        self.getSquare(7, 6).addPiece('white', 'pawn')

        # Black
        self.getSquare(0, 0).addPiece('black', 'rook')
        self.getSquare(1, 0).addPiece('black', 'knight')
        self.getSquare(2, 0).addPiece('black', 'bishop')
        self.getSquare(3, 0).addPiece('black', 'king')
        self.getSquare(4, 0).addPiece('black', 'queen')
        self.getSquare(5, 0).addPiece('black', 'bishop')
        self.getSquare(6, 0).addPiece('black', 'knight')
        self.getSquare(7, 0).addPiece('black', 'rook')
        self.getSquare(0, 1).addPiece('black', 'pawn')
        self.getSquare(1, 1).addPiece('black', 'pawn')
        self.getSquare(2, 1).addPiece('black', 'pawn')
        self.getSquare(3, 1).addPiece('black', 'pawn')
        self.getSquare(4, 1).addPiece('black', 'pawn')
        self.getSquare(5, 1).addPiece('black', 'pawn')
        self.getSquare(6, 1).addPiece('black', 'pawn')
        self.getSquare(7, 1).addPiece('black', 'pawn')

    def pieceAtSquare(self, player, str_pos):
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

                    if self.getSquare(pos.getX(), pos.getY()).getPiece().getColor() == player:
            
                        if isinstance(self.board[pos.getY()][pos.getX()].getPiece(), Piece):
                            alias_piece = self.board[pos.getY()][pos.getX()].getPiece()
                            alias_piece.setMoves(alias_piece.generateMoves(self.board[pos.getY()][pos.getX()], self))

                            print("Piece", alias_piece, "at [" + str(pos.getX()), str(pos.getY()) + "]")
                            print("Possible moves: ", end = "")
                            for move in alias_piece.getMoves():
                                print(self.columns[move.getX()] + self.rows[move.getY()] + " ", end = "")
                            print()

                            return True
                        else:
                            # there is not a piece at that square
                            return False
                    else:
                        # trying to move the other player's piece
                        return False
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
        """
        Board String String -> Boolean
        
        Return true if destination is a possible move for Piece at origin
        """
        if len(destination) < 3:
            
            if (destination[0] in self.columns) or (destination[0] in self.rows):
                
                if (destination[1] in self.columns) or (destination[1] in self.rows):
                    org_pos = self.getPositionOfSquare(origin)
                    des_pos = self.getPositionOfSquare(destination)
                    
                    if des_pos.isPositionInList(self.getBoard()[org_pos.getY()][org_pos.getX()].getPiece().getMoves()):
                        return True
                        """
                        if isinstance(self.getBoard()[des_pos.getY()][des_pos.getX()].getPiece(), Piece):
                            
                            if self.getBoard()[des_pos.getY()][des_pos.getX()].getPiece().getColor() == \
                               self.getBoard()[org_pos.getY()][org_pos.getX()].getPiece().getColor():
                                # print("You already have a piece at that location")
                                return False
                            
                            else:
                                return True
                        
                        else:
                            return True
                        """
                    else:
                        print("Piece can't move there")
                        return False
        
                else:
                    print("Index 1 of destination,", destination, ", is not in", self.columns, "or", self.rows)
                    return False
            else:
                print("Index 0 of destination,", destination, ", is not in", self.columns, "or", self.rows)
                return False
        else:
            print("destination,", destination, ", is bigger than 3 characters")
            return False

    def getPositionOfSquare(self, str_pos):
            """
            Board String -> Position

            return Square object at that position in board
            """
            if str_pos[0] in self.columns:
                position = Position(self.columns.index(str_pos[0]), self.rows.index(str_pos[1]))
                return position
            else:
                position = Position(self.columns.index(str_pos[1]), self.rows.index(str_pos[0]))
                return position

    def movePiece(self, origin, destination):
        """
        Board Position Position -> [Mutates self.Board]

        Moves the piece at origin to destination
        """
        origin_square = self.getSquare(origin.getX(), origin.getY())
        destination_square = self.getSquare(destination.getX(), destination.getY())

        if isinstance(destination_square.getPiece(), Piece):
            self.addCapturedPiece(destination_square.getPiece())
            destination_square.setPiece(origin_square.getPiece())
            origin_square.setPiece("--")
        else:
            destination_square.setPiece(origin_square.getPiece())
            origin_square.setPiece("--")