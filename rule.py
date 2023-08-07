SIZE = 8
WIDTH = SIZE
HEIGHT = SIZE

class Color:
    """色を管理するクラス
    
    Args:
        black(int): 黒,0
        white (int): 白,1
        empty (int): 指定なし,2
    """
    black = 0
    white = 1
    empty = 2
    
class Person:
    """プレイヤーを管理クラス
    
    Args:
        color (str): 碁の色情報
    """
    def __init__(self, color):
        self.color = color

def Person_of(color):
    """プレイヤーを管理クラスを作成する関数
    
    Args:
        color (str): 碁の色情報
        
    Returns:
        Person:指定した色情報を持つPersonクラス変数
    """
    return Person(color)

board = [[Color.empty for _ in range(WIDTH)] for _ in range(HEIGHT)]
change = [[-1 for _ in range(2)] for _ in range(21)]

def resetBoard():
    """盤面を初期状態に戻す
    
    Args:
        board ([Color][Color]): 各位置の碁の色情報を格納する配列
    """
    for i in range(HEIGHT):
        for j in range(WIDTH):
            board[i][j] = Color.empty
            if ((i == HEIGHT//2 and j == WIDTH//2) or (i == HEIGHT//2 - 1 and j == WIDTH//2 - 1)):
                board[i][j] = Color.black
            elif ((i == HEIGHT//2 - 1 and j == WIDTH//2) or (i == HEIGHT//2 and j == WIDTH//2 - 1)):
                board[i][j] = Color.white

def resetChange():
    """色の変わる場所を初期状態に戻す
    
    Args:
        change (list[int][int]): 色の変わる場所を格納する配列
    """
    for i in range(21):
        for j in range(2):
            change[i][j] = -1

def printColor(color):
    """碁をプリント
    
    Args:
        color (Color): 碁の色
    """
    if color == Color.black:
        print("○ ", end="")
    elif color == Color.white:
        print("● ", end="")
    else:
        print("  ", end="")

def printBoard():
    """盤面を初期状態に戻す
    
    Args:
        board (list[Color][Color]): 各位置の碁の色情報を格納する配列
    """
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
    """チェックの結果を示すクラス
    
    Args:
        OK (int): 0
        NG (int): 1
    """
    OK = 0
    NG = 1
    
def check(x, y, color):
    """碁を置けるかチェックする
    
    Args:
        num (int): 色の変わる碁の数
        ret (int): 色の変わる碁が一つでもあれば1．なければ0．
        board (list[Color][Color]): 各位置の碁の色情報を格納する配列
        change (list[Color][Color]): 各位置の碁の色情報を格納する配列
    """
    global num
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
    """盤面の変更が必要であれば変更する
        変更がなければ変更が可能な座標を表示
    """
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
    """パスするかどうか
    
    Args:
        YES (int): 0
        NO (int): 1
    """
    Yes = 0
    No = 1

def path(color):
    """パスするかどうか
    
    Returns:
        Path:Yes or No
    """
    for i in range(1, HEIGHT + 1):
        for j in range(1, WIDTH + 1):
            if check(i, j, color) == Check.OK:
                return Path.No
            elif i == HEIGHT and j == WIDTH:
                return Path.Yes