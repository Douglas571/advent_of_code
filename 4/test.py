import unittest
from bingo import *

class TestStringMethods(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      numbers, boards = extrar_input(f.readline())

      exp_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
      exp_boards = []
      self.assertEqual(exp_numbers, numbers)
      self.assertEqual(exp_boards, boards)

      winner = bingo_game(numbers, boards)
      
if __name__ == '__main__':
  unittest.main()