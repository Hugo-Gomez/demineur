from random import randint
import sys

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
                action = input(">> Press d to dig or f to flago r unflag ; e to exit game : ")
                if not isinstance(action, str) or len(action) > 1:
                    if action != "d" or action != "f" or action != "e":
                        raise ValueError
                goodInstruction = True
                return action
            except:
                print("/!\ Bad format, try again\n")

    def smartDig(self, row, col):
        el = self.board[col][row]

        if el.value == ".":
            el.dig()
            if el.content == 0:
                if row != 0 and col != 0:
                    # haut gauche
                    self.smartDig(row-1, col-1)
                if row != 0:
                    # haut
                    self.smartDig(row-1, col)
                if row != 0 and col != self.nbSquare -1:
                    # haut droite
                    self.smartDig(row-1, col+1)
                if col != self.nbSquare -1:
                    # droite
                    self.smartDig(row, col+1)
                if row != self.nbSquare -1 and col != self.nbSquare -1:
                    # bas droite
                    self.smartDig(row+1, col+1)
                if row != self.nbSquare -1:
                    # bas
                    self.smartDig(row+1, col)
                if row != self.nbSquare -1 and col != 0:
                    # bas gauche
                    self.smartDig(row+1, col-1)
                if col != 0:
                    # gauche
                    self.smartDig(row, col-1)

    def makeMove(self):
        action = self.chooseAction()

        if action == "e":
            sys.exit("Game exited by player")
        else:
            move, el = False, False
            try:
                move = input(">> Your move in this format -> 00 : ")
                print("\n")
                if len(move) > 2:
                    raise ValueError
                move = [int(i) for i in move]
                el = self.board[move[0]][move[1]]
            except:
                print("/!\ Bad format or invalid coordinates\n")
            if move is not False and el is not False:
                if action == "d":
                    if el.value != "@":
                        self.smartDig(move[1], move[0])
                    else:
                        print("/!\ Position marked, remove flag to dig.")
                elif action == "f":
                    if el.value == "." or el.value == "@":
                        el.mark()
                    else:
                        print("/!\ Position already discovered.")
                return move, action

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