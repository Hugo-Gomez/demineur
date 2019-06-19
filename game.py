from classes.board import Board
from classes.ascii_art import AsciiArt

AsciiArt().printTitle()
print("By hugomez\n")
board = Board(3, 1)
board.initBoard()
while not board.finished:
    print("------------------------------------------------------------------\n")
    board.printBoard()
    print("\n")
    move = board.makeMove()
    board.checkStatus(move)