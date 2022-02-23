import unittest
from bingo import *

class Test(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    #print()
    #print('---- Test 1 ----')
    #print()
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
      self.assertEqual(3, results["winner"])
      self.assertEqual(24, results["last_number"])
      self.assertEqual(188, results["sum_unmarked_numbers"])
      self.assertEqual([14, 21, 17, 24, 4], results["completed"])
      self.assertEqual("row 1", results["completed_a"])
      self.assertEqual(4512, results["score"])
      
  def test_two_col(self):
    #print()
    #print('---- Test 2 ----')
    #print()
    with open('example2.txt') as f:
      raw_lines = f.readlines()
      numbers, boards = extract_input(raw_lines)

      res = bingo_game(numbers, boards)
      #print('Results 1th part:')
      #for k, v in res.items():
        #print(f'    {k}: {v}')

      self.assertEqual(res['completed'], [22, 8, 21, 6, 1])
      self.assertEqual(res['winner'], 1)
      self.assertEqual(res['completed_a'], 'colum 1')
      
  #@unittest.skip 
  def test_three_trunkated(self):
    #----- trunkated bingo game -----#
    with open('example.txt') as f:
      raw_lines = f.readlines()
      numbers, boards = extract_input(raw_lines)

      results = trunkated_bingo_game(numbers, boards)
      last_winner = results[-1]

      self.assertEqual(last_winner["board"], 2)
      self.assertEqual(last_winner['score'], 1924)

      """
      self.assertEqual(2, results["winner"])
      self.assertEqual(13, results["last_number"])
      self.assertEqual(148, results["sum_unmarked_numbers"])
      self.assertEqual([0, 13, 7, 10, 16], results["completed"])
      self.assertEqual("colum 3", results["completed_a"])
      self.assertEqual(1924, results["score"])      
      """
if __name__ == '__main__':
  unittest.main()