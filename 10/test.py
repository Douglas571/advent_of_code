import unittest
from smoke_basin import *

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      

      # End part:
      solution = get_1th_solution(raw_lines)
      self.assertEqual(solution, 26397)

  #@unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

if __name__ == '__main__':
  unittest.main()