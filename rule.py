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
change = [[-1 for _ in range(2)] for _ in range(21)]

def resetBoard():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            board[i][j] = Color.empty
            if ((i == HEIGHT//2 and j == WIDTH//2) or (i == HEIGHT//2 - 1 and j == WIDTH//2 - 1)):
                board[i][j] = Color.black
            elif ((i == HEIGHT//2 - 1 and j == WIDTH//2) or (i == HEIGHT//2 and j == WIDTH//2 - 1)):
                board[i][j] = Color.white

def printColor(color):
    if color == Color.black:
        print("○ ", end="")
    elif color == Color.white:
        print("● ", end="")
    else:
        print("  ", end="")