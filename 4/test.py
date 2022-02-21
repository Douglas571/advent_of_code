import unittest
from bingo import *

class TestStringMethods(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()
      numbers, boards = extract_input(raw_lines)

      exp_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
      exp_boards = [
        [
          [22, 13, 17, 11, 0],
          [8, 2, 23, 4, 24],
          [21, 9, 14, 16, 7],
          [6, 10, 3, 18, 5],
          [1, 12, 20, 15, 19],
        ],
        [
          [3, 15, 0, 2, 22],
          [9, 18, 13, 17, 5],
          [19, 8, 7, 25, 23],
          [20, 11, 10, 24, 4],
          [14, 21, 16, 12, 6],
        ],
        [
          [14, 21, 17, 24, 4],
          [10, 16, 15, 9, 19],
          [18, 8, 23, 26, 20],
          [22, 11, 13, 6, 5],
          [2, 0, 12, 3, 7],
        ]
      ]
      self.assertEqual(exp_numbers, numbers)
      self.assertEqual(exp_boards, boards)

      results = bingo_game(numbers, boards)
      self.assertEqual(3, results.winner_board)
      self.assertEqual(24, results.last_number)
      self.assertEqual(180, results.sum_unmarket_numbs)
      
if __name__ == '__main__':
  unittest.main()