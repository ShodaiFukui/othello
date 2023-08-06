SIZE = 8
WIDTH = SIZE
HEIGHT = SIZE

class Color:
    black = 0
    white = 1
    empty = 2
    
class Person:
    def __init__(self, color):
        self.color = color

board = [[Color.empty for _ in range(WIDTH)] for _ in range(HEIGHT)]


def resetBoard():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            board[i][j] = Color.empty
            if ((i == HEIGHT//2 and j == WIDTH//2) or (i == HEIGHT//2 - 1 and j == WIDTH//2 - 1)):
                board[i][j] = Color.black
            elif ((i == HEIGHT//2 - 1 and j == WIDTH//2) or (i == HEIGHT//2 and j == WIDTH//2 - 1)):
                board[i][j] = Color.white

def resetChange():
    for i in range(21):
        for j in range(2):
            change[i][j] = -1

def printColor(color):
    if color == Color.black:
        print("○ ", end="")
    elif color == Color.white:
        print("● ", end="")
    else:
        print("  ", end="")

def printBoard():
    resetChange()
    print("  ", end="")
    for i in range(SIZE):
        print(f"{i + 1} ", end="")
    print()
    for i in range(HEIGHT):
        print(f"{i + 1} ", end="")
        for j in range(WIDTH):
            printColor(board[i][j])
        print()