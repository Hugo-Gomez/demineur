from random import randint

from classes.square import Square

class Board:
    def __init__(self):
        self.board = []

    def getBoard(self):
        return self.board

    def initBoard(self, nbSquare, nbBomb):
        nbSquareRange = range(0, nbSquare)
        bombCntr = 0
        bombsCoordinates = []
        for row in nbSquareRange:
            self.board.append([Square() for i in nbSquareRange])
        while not bombCntr == nbBomb:
            r1 = randint(0, nbSquare - 1)
            r2 = randint(0, nbSquare - 1)
            if not self.board[r1][r2].isBomb():
                self.board[r1][r2].setBomb()
                bombsCoordinates.append((r1, r2))
                bombCntr += 1
        # Debug
        #print("Bombs location : {}".format(bombsCoordinates))
        #print("--------------")
        # Code
        for bomb in bombsCoordinates:
            # Debug
            #print("{} // {}".format(self.board[bomb[0]][bomb[1]].content, bomb))
            #print("--------------")
            # Code
            try:
                if bomb[0] != 0:
                    self.board[bomb[0] - 1][bomb[1]].incrContent()
                    if bomb[1] != 0:
                        self.board[bomb[0] - 1][bomb[1] - 1].incrContent()
                    if bomb[1] != (nbSquare - 1):
                        self.board[bomb[0] - 1][bomb[1] + 1].incrContent()
                if bomb[0] != (nbSquare - 1):
                    self.board[bomb[0] + 1][bomb[1]].incrContent()
                    if bomb[1] != 0:
                        self.board[bomb[0] + 1][bomb[1] - 1].incrContent()
                    if bomb[1] != (nbSquare - 1):
                        self.board[bomb[0] + 1][bomb[1] + 1].incrContent()
                if bomb[1] != 0:
                    self.board[bomb[0]][bomb[1] - 1].incrContent()
                if bomb[1] != (nbSquare - 1):
                    self.board[bomb[0]][bomb[1] + 1].incrContent()
            except:
                print("An exception occurred")



    def printBoard(self):
        for row in self.board:
            print("{}".format(str([i.content for i in row]).replace(",", "").replace("'", "")))