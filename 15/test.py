import unittest
from chiton import *

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      solution = get_1th_solution(raw_lines)
      self.assertEqual(solution, 40)

  @unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      # solution = get_2th_solution(raw_lines)
      # self.assertEqual(solution, 0000)

if __name__ == '__main__':
  unittest.main()