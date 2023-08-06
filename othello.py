import rule
import gameFlow
import printResult

def main():
    rule.resetBoard()
    rule.printBoard()
    while True:
        mode = input("モード選択. 0..検証用/1..プレイ: ")
        choice = input("あなたの碁の色を入力して下さい. 'black' or 'white': ")
        if choice == "black":
            player = rule.Person_of(rule.Color.black)
            npc = rule.Person_of(rule.Color.white)
        elif choice == "white":
            player = rule.Person_of(rule.Color.white)
            npc = rule.Person_of(rule.Color.black)
        else:
            print("'black'または'white'を入力して下さい．")
            continue
        break
    
    gameFlow.game(player.color, npc.color, mode)
    printResult.result(player.color)
    printResult.printOut()

if __name__ == "__main__":
    main()