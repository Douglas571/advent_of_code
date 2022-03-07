import unittest
from syntax_scoring import *

import math

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      exp_errors = {
        ")": 2,
        "]": 1,
        "}": 1,
        ">": 1
      }

      lines = get_input(raw_lines)
      errors_found, _ = check(lines)
      self.assertEqual(errors_found, exp_errors)

      # End part:
      solution = get_1th_solution(raw_lines)
      self.assertEqual(solution, 26397)

  #@unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      # End 
      solution = get_2th_solution(raw_lines)
      self.assertEqual(solution, 288957)

if __name__ == '__main__':
  unittest.main()