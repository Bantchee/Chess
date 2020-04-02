from Components.board import Board as brd

# coolness
def dialogueTree(player):
    first_message = str(input("\nPlayer " + player + " - type 'move', 'captured pieces', or 'quit': ")).lower()
    
    if first_message == 'move':
        return movementDialogue(player)

    elif first_message == 'captured pieces':
        return capturedPiecesDialogue(player)

    elif first_message == 'quit':
        return quitDialogue(player)
    else:
        print("\nWrong input, try again.")
        return dialogueTree(player)

def movementDialogue(player):
    origin = str(input("\nType in the location of the piece you want to move or type 'back': ")).lower()

    if b.pieceAtSquare(player, origin):
        destination = str(input("\nType in where you want to move the piece or type 'back': ")).lower()
        
        if b.possibleMove(origin, destination):
            origin = b.getPositionOfSquare(origin)
            destination = b.getPositionOfSquare(destination)
            b.movePiece(origin, destination)
            return False

        elif destination == 'back':
            return dialogueTree(player)
        
        else:
            print("\nTry again")
            return movementDialogue(player)
    
    elif origin == 'back':
        return dialogueTree(player)
    
    else:
        print("\nTry again")
        return movementDialogue(player)

def capturedPiecesDialogue(player):
    if player == 'white':
        print(b.getCapturedPieces('black'))
    else:
        print(b.getCapturedPieces('white'))
    return dialogueTree(player)

def quitDialogue(player):
    if player == 'white':
        print('\nPlayer black wins!')
    else:
        print('\nPlayer white wins!')
    return True
    # print captured pieces at end

def startGame():
    quit = False
    while not quit:
        
        print()

        # White player's turn
        # print updated board
        for char in b.columns:
             print(" ", char, end = "")
        print()

        for row in b.getBoard():
            print(b.getBoard().index(row) + 1, end = " ")
            for sqr in row:
                print(sqr, end = " ")
            print()

        # Dialogue tree for player white
        # not working
        if dialogueTree('white'):
            quit = True
            continue

        # Black player's turn
        # print updated board
        for char in b.columns:
             print(" ", char, end = "")
        print()

        for row in b.getBoard():
            print(b.getBoard().index(row) + 1, end = " ")
            for sqr in row:
                print(sqr, end = " ")
            print()

        # Dialogue tree for player black
        if dialogueTree('black'):
            quit = True
            continue

b = brd()

startGame()