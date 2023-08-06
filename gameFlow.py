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
            
            checkResult = rule.check(x, y, my_color)
            rule.putGo(x, y, my_color)
            if checkResult == rule.Check.OK:
                print(f"({x},{y})に碁を置きました．")
                rule.printBoard()
                break

def npcTurn(npc_color): 
    print("\n＜コンピュータのターン＞")
    if rule.path(npc_color) == rule.Path.Yes:
        print("碁を置くところがありません．\nパスします．")
    else:
        while True:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if rule.check(x, y, npc_color) == rule.Check.OK:
                rule.putGo(x, y, npc_color)
                print(f"({x},{y})に碁を置きました．")
                rule.printBoard()
                break

def game(my_color, npc_color, mode):
    if(mode == "0"):
        while True:
            npcTurn(my_color)
            npcTurn(npc_color)
            if rule.path(my_color) == rule.Path.Yes and rule.path(npc_color) == rule.Path.Yes:
                print("ゲームセット！")
                break
    else:
        while True:
            myTurn(my_color)
            npcTurn(npc_color)
            if rule.path(my_color) == rule.Path.Yes and rule.path(npc_color) == rule.Path.Yes:
                print("ゲームセット！")
                break