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

def Person_of(color):
    return Person(color)

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

class Check:
    OK = 0
    NG = 1
    
num = 0
def check(x, y, color):
    num = 0
    ret = 0
    if board[y - 1][x - 1] != Color.empty:
        return Check.NG
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y - 1 + i < 0 or y - 1 + i >= HEIGHT:
                continue
            if x - 1 + j < 0 or x - 1 + j >= WIDTH:
                continue
            if board[y - 1 + i][x - 1 + j] == color:
                continue
            if board[y - 1 + i][x - 1 + j] != color and board[y - 1 + i][x - 1 + j] != Color.empty:
                times = 1
                while not (y - 1 + times * i < 0 or y - 1 + times * i >= HEIGHT or x - 1 + times * j < 0 or x - 1 + times * j >= WIDTH):
                    if board[y - 1 + times * i][x - 1 + times * j] == Color.empty:
                        break
                    if board[y - 1 + times * i][x - 1 + times * j] != color:
                        times += 1
                        continue
                    if board[y - 1 + times * i][x - 1 + times * j] == color:
                        for l in range(times):
                            change[num][0] = y - 1 + l * i
                            change[num][1] = x - 1 + l * j
                            num += 1
                        ret = 1
                        break
    if ret == 1:
        return Check.OK
    else:
        return Check.NG

def putGo(x, y, color):
    if check(x, y, color) == Check.OK:
        for i in range(num):
            board[change[i][0]][change[i][1]] = color
    else:
        print(f"({x},{y})に碁を置くことはできません．\n以下の座標に置くことができます．")
        for j in range(1, HEIGHT + 1):
            for k in range(1, WIDTH + 1):
                if check(j, k, color) == Check.OK:
                    print(f"({j}, {k})")

class Path:
    Yes = 0
    No = 1

def path(color):
    for i in range(1, HEIGHT + 1):
        for j in range(1, WIDTH + 1):
            if check(i, j, color) == Check.OK:
                return Path.No
            elif i == HEIGHT and j == WIDTH:
                return Path.Yes