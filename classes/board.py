from random import randint

from classes.square import Square
from classes.ascii_art import AsciiArt

class Board:

    def __init__(self, nbSquare, nbBomb):
        self.board = []
        self.nbSquare = nbSquare
        self.nbBomb = nbBomb
        self.finished = False

    def chooseAction(self):
        goodInstruction = False
        while not goodInstruction:
            try:
                action = input(">> Press d to dig or f to flag : ")
                if not isinstance(action, str) or len(action) > 1:
                    if action != "d" or action != "f":
                        raise ValueError
                goodInstruction = True
                return action
            except:
                print("/!\ Bad format, try again\n")

    def makeMove(self):
        action = self.chooseAction()
        try:
            move = input(">> Your move in this format -> 00 : ")
            print("\n")
            if len(move) > 2:
                raise ValueError
            move = [int(i) for i in move]
            el = self.board[move[0]][move[1]]
            if action == "d":
                if el.value != "@":
                    el.dig()
                else:
                    print("/!\ Position marked, remove flag to dig.")
                    raise ValueError
            elif action == "f":
                if el.value == "." or el.value == "@":
                    el.mark()
                else:
                    print("/!\ Position already discovered.")
                    raise ValueError
            return move, action
        except:
            print("/!\ Bad format or invalid coordinates\n")

    def checkStatus(self, move):
        bombCounter = 0
        for row in self.board:
            row = [i.value for i in row]
            bombCounter += row.count(".")
            bombCounter += row.count("@")
        if move:
            move, action = move
            if self.board[move[0]][move[1]].content == "B" and action == "d" :
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