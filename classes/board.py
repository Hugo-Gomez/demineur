from random import randint
import sys

from classes.square import Square
from classes.ascii_art import print_loose, print_win


class Board:

    def __init__(self, nb_square, nb_bomb):
        self.board = []
        self.nb_square = nb_square
        self.nb_bomb = nb_bomb
        self.finished = False

    @staticmethod
    def choose_action():
        good_instruction = False
        while not good_instruction:
            try:
                action = input(">> Press d to dig ; f to flag or remove flag ; e to exit game : ")
                if len(action) > 1 or action not in ["d",  "f", "e"]:
                    raise ValueError
                good_instruction = True
                return action
            except ValueError:
                print("/!\ Bad format, try again\n")

    def smart_dig(self, row, col):
        el = self.board[col][row]

        if el.value == ".":
            el.dig()
            if el.content == 0:
                if row != 0 and col != 0:
                    # haut gauche
                    self.smart_dig(row-1, col-1)
                if row != 0:
                    # haut
                    self.smart_dig(row-1, col)
                if row != 0 and col != self.nb_square - 1:
                    # haut droite
                    self.smart_dig(row-1, col+1)
                if col != self.nb_square - 1:
                    # droite
                    self.smart_dig(row, col+1)
                if row != self.nb_square - 1 and col != self.nb_square - 1:
                    # bas droite
                    self.smart_dig(row+1, col+1)
                if row != self.nb_square - 1:
                    # bas
                    self.smart_dig(row+1, col)
                if row != self.nb_square - 1 and col != 0:
                    # bas gauche
                    self.smart_dig(row+1, col-1)
                if col != 0:
                    # gauche
                    self.smart_dig(row, col-1)

    def make_move(self):
        action = self.choose_action()

        if action == "e":
            sys.exit("Game exited by player")
        else:
            move, el = 0, 0
            valid_coordinates = False
            while not valid_coordinates:
                try:
                    move = input(">> Your move in this format -> 0,0 : ")
                    print("\n")
                    move = move.split(",")
                    move = [int(i) for i in move]
                    el = self.board[move[0]][move[1]]
                    valid_coordinates = True
                except:
                    print("/!\ Bad format or invalid coordinates\n")

            if action == "d":
                if el.value != "@":
                    self.smart_dig(move[1], move[0])
                else:
                    print("/!\ Position marked, remove flag to dig.")
            elif action == "f":
                if el.value == "." or el.value == "@":
                    el.mark()
                else:
                    print("/!\ Position already discovered.")
            return move, action

    def check_status(self, move):
        bomb_counter = 0
        for row in self.board:
            row = [i.value for i in row]
            bomb_counter += row.count(".")
            bomb_counter += row.count("@")
        if move:
            move, action = move
            if self.board[move[0]][move[1]].content == "B" and action == "d":
                self.print_board()
                print("BOUUUM !!!")
                print_loose()
                self.finished = True
            elif bomb_counter == self.nb_bomb:
                self.print_board()
                print_win()
                print("GG WP")
                self.finished = True

    def init_board(self):
        bomb_counter = 0
        bombs_coordinate = []
        for _ in range(0, self.nb_square):
            self.board.append([Square() for _ in range(0, self.nb_square)])
        while not bomb_counter == self.nb_bomb:
            r1 = randint(0, self.nb_square - 1)
            r2 = randint(0, self.nb_square - 1)
            if not self.board[r1][r2].is_bomb():
                self.board[r1][r2].set_bomb()
                bombs_coordinate.append((r1, r2))
                bomb_counter += 1
        for bomb in bombs_coordinate:
            if bomb[0] != 0:
                self.board[bomb[0] - 1][bomb[1]].increment_content()
                if bomb[1] != 0:
                    self.board[bomb[0] - 1][bomb[1] - 1].increment_content()
                if bomb[1] != (self.nb_square - 1):
                    self.board[bomb[0] - 1][bomb[1] + 1].increment_content()
            if bomb[0] != (self.nb_square - 1):
                self.board[bomb[0] + 1][bomb[1]].increment_content()
                if bomb[1] != 0:
                    self.board[bomb[0] + 1][bomb[1] - 1].increment_content()
                if bomb[1] != (self.nb_square - 1):
                    self.board[bomb[0] + 1][bomb[1] + 1].increment_content()
            if bomb[1] != 0:
                self.board[bomb[0]][bomb[1] - 1].increment_content()
            if bomb[1] != (self.nb_square - 1):
                self.board[bomb[0]][bomb[1] + 1].increment_content()

    def print_board(self):
        for row in self.board:
            print("{}".format(str([i.value for i in row]).replace(",", "").replace("'", "")))
