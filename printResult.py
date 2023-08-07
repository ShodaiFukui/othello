import rule

def result(my_color):
    """結果を表示
    
    Args:
        my_color (Color): プレイヤーのカラー
        sumOfBlack (int): 最後の盤面での黒の数
        sumOfWhite (int): 最後の盤面での白の数
    """
    sumOfBlack = sum([1 for row in rule.board for cell in row if cell == rule.Color.black])
    sumOfWhite = sum([1 for row in rule.board for cell in row if cell == rule.Color.white])
    print("\n＜集計結果＞")
    print(f"black : {sumOfBlack}個")
    print(f"white : {sumOfWhite}個")
    if sumOfBlack > sumOfWhite and my_color == rule.Color.black:
        print("あなたの勝ち!")
    elif sumOfWhite > sumOfBlack and my_color == rule.Color.white:
        print("あなたの勝ち!")
    elif sumOfBlack > sumOfWhite and my_color == rule.Color.white:
        print("NPCの勝ち!")
    elif sumOfWhite > sumOfBlack and my_color == rule.Color.black:
        print("NPCの勝ち!")
    else:
        print("引き分け")

def printOut():
    """結果をテキストデータとして出力する
    
    Args:
        sumOfBlack (int): 最後の盤面での黒の数
        sumOfWhite (int): 最後の盤面での白の数
    """
    with open("result.txt", "w") as fp:
        fp.write("  ")
        for i in range(rule.SIZE):
            fp.write(f"{i + 1} ")
        fp.write("\n")
        for i in range(rule.HEIGHT):
            fp.write(f"{i + 1} ")
            for j in range(rule.WIDTH):
                if rule.board[i][j] == rule.Color.black:
                    fp.write("○ ")
                elif rule.board[i][j] == rule.Color.white:
                    fp.write("● ")
                else:
                    fp.write("  ")
            fp.write("\n")
        sumOfBlack = sum([1 for row in rule.board for cell in row if cell == rule.Color.black])
        sumOfWhite = sum([1 for row in rule.board for cell in row if cell == rule.Color.white])
        fp.write("\n＜集計結果＞\n")
        fp.write(f"black : {sumOfBlack}個\nwhite : {sumOfWhite}個\n")
        if sumOfBlack > sumOfWhite:
            fp.write("黒の勝ち!\n")
        elif sumOfWhite > sumOfBlack:
            fp.write("白の勝ち!\n")
        else:
            fp.write("引き分け\n")