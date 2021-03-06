import discord
import asyncio

class Space:

    def __init__(self, spaceColor, piece):
        self.spaceColor = spaceColor
        self.piece = piece

    def fillSpace(self):
        self.piece = True

    def emptySpace(self):
        self.piece = False

class Piece:

    def __init__(self, pieceColor, xPos, yPos, king):
        self.pieceColor = pieceColor
        self.xPos = xPos
        self.yPos = yPos
        self.king = king

    def move(self, newXPos, newYPos):
        if newXPos - self.xPos == 0:
            return False
        elif newXPos - self.xPos > 1 or newXPos - self.xPos < -1:
            return False
        elif newXPos - self.xPos == -1 or newXPos - self.xPos == 1:
            if newYPos - self.yPos == 0:
                return False
            elif newYPos - self.yPos > 1 or newYPos - self.yPos < -1:
                return False
            elif newYPos - self.yPos == 1:
                if self.pieceColor == "white":
                    return True
                elif self.pieceColor == "black" and self.king == True:
                    return True
                else:
                    return False
            elif newYPos - self.yPos == -1:
                if self.pieceColor == "black":
                    return True
                elif self.pieceColor == "white" and self.king == True:
                    return True
                else:
                    return False
        
        if newYPos == 7 and self.pieceColor == "white":
            self.kingPiece()
        elif newYPos == 0 and self.pieceColor == "black":
            self.kingPiece()
    
    def kingPiece(self):
        self.king = True

client = discord.Client()

board = [[range(7)],[range(7)]]

for x in range(1, 7, 2):
    for y in range(0, 6, 2):
        board[x][y] = Space("white", False)
        board[x][y] = Piece("black", x, y, False)

for x in range(0, 6, 2):
    for y in range(1, 7, 2):
        board[x][y] = Space("black", False)
        board[x][y] = Piece("white", x, y, False)
