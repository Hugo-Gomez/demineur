from classes.board import Board
from classes.ascii_art import AsciiArt

AsciiArt().printTitle()
print("Welcome to the game. Rules are simple : \n")
print("""\
- You have to find bombs on the field
- If you dig a bomb, game is over
- You have to dig every position (except bombed ones) to win the game
- You can put a flag on a position if you think there is a bomb, if you want to dig that position anyway, you have to remove the flag first
Enjoy !
""")
print("By hugomez\n")
board = Board(3, 1)
board.initBoard()
while not board.finished:
    print("------------------------------------------------------------------\n")
    board.printBoard()
    print("\n")
    move = board.makeMove()
    board.checkStatus(move)