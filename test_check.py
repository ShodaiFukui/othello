import unittest
import rule

#以下の盤面でのテストを行う
#   1 2 3 4 5 6 7 8
# 1
# 2
# 3         ○ ●
# 4       ○ ● ●
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
        
    def test_check3(self):
        result = rule.check(4, 3, rule.Color.black)
        self.assertEqual(rule.Check.NG, result)
    
    def test_check4(self):
        result = rule.check(4, 3, rule.Color.white)
        self.assertEqual(rule.Check.OK, result)
    
    def test_check5(self):
        result = rule.check(3, 6, rule.Color.black)
        self.assertEqual(rule.Check.NG, result)
        
    def test_check6(self):
        result = rule.check(3, 6, rule.Color.white)
        self.assertEqual(rule.Check.NG, result)
    
    def test_check7(self):
        result = rule.check(4, 2, rule.Color.black)
        self.assertEqual(rule.Check.NG, result)
        
    def test_check8(self):
        result = rule.check(4, 2, rule.Color.white)
        self.assertEqual(rule.Check.OK, result)

if __name__ == "__main__":
    rule.resetBoard()
    rule.board[2][4] = rule.Color.black
    rule.board[2][5] = rule.Color.white
    rule.board[3][5] = rule.Color.white
    unittest.main()