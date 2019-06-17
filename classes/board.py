from random import randint

from classes.square import Square

class Board:
    def __init__(self):
        self.board = []

    def getBoard(self):
        return self.board

    def initBoard(self, nbSquare, nbBomb):
        nbSquareRange = range(0, nbSquare)
        nbBombRange = range(0, nbBomb)
        bombCntr = 0
        for row in nbSquareRange:
            self.board.append([Square() for i in nbSquareRange])
        while not bombCntr == 3:
            r1 = randint(0, nbSquare - 1)
            r2 = randint(0, nbSquare - 1)
            if not self.board[r1][r2].isBomb():
                self.board[r1][r2].setBomb()
                bombCntr += 1
            else:
                continue


    def printBoard(self):
        for row in self.board:
            print("{}\n".format([i.content for i in row]))