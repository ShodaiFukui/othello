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