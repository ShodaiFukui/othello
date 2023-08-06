import unittest
import rule

#以下の盤面でのテストを行う
#   1 2 3 4 5 6 7 8
# 1
# 2
# 3         ○ ●
# 4       ○ ●
# 5       ● ○
# 6
# 7
# 8

class TestMyTest(unittest.TestCase):
    
    def test_check1(self):
        result = rule.check(1, 1, rule.Color.black)
        self.assertEqual(rule.Check.NG, result)
    
    def test_check2(self):
        result = rule.check(1, 1, rule.Color.white)
        self.assertEqual(rule.Check.NG, result)
        
if __name__ == "__main__":
    rule.resetBoard()
    rule.board[4][2] = rule.Color.black
    rule.board[5][2] = rule.Color.white
    unittest.main()