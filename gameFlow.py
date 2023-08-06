import rule
import random

def myTurn(my_color):
    
    print("\n＜あなたのターン＞")
    if rule.path(my_color) == rule.Path.Yes:
        print("碁を置くところがありません．\nパスします．")
    else:
        while True:
            x = -1
            y = -1
            while True:
                x = int(input("x座標(1~8) : "))
                if x < 1 or x > 8:
                    print("1~8の整数で答えてください．")
                    continue
                break
            while True:
                y = int(input("y座標(1~8) : "))
                if y < 1 or y > 8:
                    print("1~8の整数で答えてください．")
                    continue
                break
            
            rule.putGo(x, y, my_color)
            if rule.check(x, y, my_color) == rule.Check.OK:
                print(f"({x},{y})に碁を置きました．")
                rule.printBoard()
                break