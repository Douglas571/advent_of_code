import unittest
from extended_polymerization import *

class Test_Case(unittest.TestCase):
  # @unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      solution = get_1th_solution(raw_lines)
      self.assertEqual(solution, 1588)

  # @unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      solution = get_2th_solution(raw_lines)
      self.assertEqual(solution, 2188189693529)

  @unittest.skip
  def test_three(self):
    with open('test.txt') as f:
      raw_lines = f.readlines()

      solution = get_1th_solution(raw_lines, 3)
      self.assertEqual(solution, 2)      

if __name__ == '__main__':
  unittest.main()