class Position(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"
    
    def getX(self):
        return self.x
    
    def setX(self, newX):
        self.x = newX
    
    def getY(self):
        return self.y
    
    def setY(self, newY):
        self.y = newY
    
    def isPositionInList(self, list_of_positions):
        """Posistion [List-of Positions] -> Boolean, Return true if self is in list_of_poitions"""
        if self in list_of_positions:
            return True
        return False
