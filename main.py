from Components.board import Board as brd

def dialogueTree(player):
    first_message = str(input("\nPlayer " + player + " - type 'move', 'captured pieces', or 'forfeit': ")).lower()
    
    if first_message == 'move':
        movementDialogue(player)

    elif first_message == 'captured pieces':
        capturedPiecesDialogue(player)

    elif first_message == 'forfeit':
        forfeitDialogue(player)
        return 'quit'
    else:
        print("\nWrong input, try again.\n")
        dialogueTree(player)

def movementDialogue(player):
    origin = str(input("\nType in the location of the piece you want to move or type 'back': ")).lower()

    if b.pieceAtSquare(origin):
        destination = str(input("\nType in where you want to move the piece or type 'back': ")).lower()
        
        if b.possibleMove(origin, destination):
            origin = b.getPositionOfSquare(origin)
            destination = b.getPositionOfSquare(destination)
            b.movePiece(player, origin, destination)
        
        elif destination == 'back':
            dialogueTree(player)
        
        else:
            print("\nTry again\n")
            movementDialogue(player)
    
    elif origin == 'back':
        dialogueTree(player)
    
    else:
        print("\nTry again\n")
        movementDialogue(player)

def capturedPiecesDialogue(player):
    print(b.getCapturedPieces(player))
    dialogueTree(player)

def forfeitDialogue(player):
    if player == 'white':
        print('\nPlayer black wins!')
    else:
        print('\nPlayer white wins!')    
    # print captured pieces at end
    
    

def startGame():
    while True:
        
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
        print()

        # Dialogue tree for player white
        # not working
        if dialogueTree('white') == 'quit':
            break

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
        print()

        # Dialogue tree for player black
        if dialogueTree('black') == 'quit':
            break

b = brd()

startGame()