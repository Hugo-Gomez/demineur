from random import randint

from classes.square import Square
from classes.ascii_art import AsciiArt

class Board:

    def __init__(self, nbSquare, nbBomb):
        self.board = []
        self.nbSquare = nbSquare
        self.nbBomb = nbBomb
        self.finished = False

    def makeMove(self):
        try:
            move = input("Your move in this format -> 00 : ")
            if len(move) > 2:
                raise ValueError
            move = [int(i) for i in move]
            self.board[move[0]][move[1]].dig()
            return move
        except:
            print("Bad format or invalid coordinates")

    def checkStatus(self, move):
        bombCounter = 0
        for row in self.board:
            bombCounter += [i.value for i in row].count(".")
        if move:
            if self.board[move[0]][move[1]].content == "B":
                self.printBoard()
                print("BOUUUM !!!")
                AsciiArt().printLoose()
                self.finished = True
            if bombCounter == self.nbBomb:
                self.printBoard()
                AsciiArt().printWin()
                print("GG WP")
                self.finished = True

    def initBoard(self):
        nbSquareRange = range(0, self.nbSquare)
        bombCntr = 0
        bombsCoordinate = []
        for row in nbSquareRange:
            self.board.append([Square() for i in nbSquareRange])
        while not bombCntr == self.nbBomb:
            r1 = randint(0, self.nbSquare - 1)
            r2 = randint(0, self.nbSquare - 1)
            if not self.board[r1][r2].isBomb():
                self.board[r1][r2].setBomb()
                bombsCoordinate.append((r1, r2))
                bombCntr += 1
        for bomb in bombsCoordinate:
            if bomb[0] != 0:
                self.board[bomb[0] - 1][bomb[1]].incrContent()
                if bomb[1] != 0:
                    self.board[bomb[0] - 1][bomb[1] - 1].incrContent()
                if bomb[1] != (self.nbSquare - 1):
                    self.board[bomb[0] - 1][bomb[1] + 1].incrContent()
            if bomb[0] != (self.nbSquare - 1):
                self.board[bomb[0] + 1][bomb[1]].incrContent()
                if bomb[1] != 0:
                    self.board[bomb[0] + 1][bomb[1] - 1].incrContent()
                if bomb[1] != (self.nbSquare - 1):
                    self.board[bomb[0] + 1][bomb[1] + 1].incrContent()
            if bomb[1] != 0:
                self.board[bomb[0]][bomb[1] - 1].incrContent()
            if bomb[1] != (self.nbSquare - 1):
                self.board[bomb[0]][bomb[1] + 1].incrContent()

    def printBoard(self):
        for row in self.board:
            print("{}".format(str([i.value for i in row]).replace(",", "").replace("'", "")))