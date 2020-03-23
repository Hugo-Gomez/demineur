from classes.board import Board
from classes.ascii_art import print_title

print_title()
print("Welcome to the game. Rules are simple : \n")
print("""\
- You have to find bombs on the field
- If you dig a bomb, game is over
- You have to dig every position (except bombed ones) to win the game
- You can put a flag on a position if you think there is a bomb, if you want to dig that position anyway, you have to remove the flag first
- Number of squares and number of bombs must obviously be greater than 0
- Number of squares must obviously be greater than number of bombs
- Number of squares -> Min : 4 // Max : 100

Enjoy !
""")
print("By hugomez\n")
squares, bombs = 0, 0
valid_board_infos = False
while not valid_board_infos:
    try:
        squares = int(input(">> Number of squares : \n"))
        if squares < 4:
            raise ValueError
        bombs = int(input(">> Number of bombs : \n"))
        if bombs > (squares**2) - 1 or bombs == 0:
            raise ValueError
        valid_board_infos = True
    except ValueError:
        print("/!\ Please enter valid numbers (checkout the rules enumerated above)")
board = Board(squares, bombs)
board.init_board()
while not board.finished:
    print("------------------------------------------------------------------\n")
    board.print_board()
    print("\n")
    move = board.make_move()
    board.check_status(move)
