import unittest
from smoke_basin import *

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()
      fm = get_floor_map(raw_lines)
      self.assertEqual(fm[0], [2,1,9,9,9,4,3,2,1,0])
      self.assertEqual(fm[-1], [9,8,9,9,9,6,5,6,7,8])

      lwps = get_lowest_points(fm)
      self.assertEqual(lwps, [1, 0, 5, 5])

      rlvs = get_risk_levels(lwps)
      self.assertEqual(rlvs, [2, 1, 6, 6])

      sum_rlvs = sum(rlvs)
      self.assertEqual(sum_rlvs, 15)

      solution = get_1th_solution(raw_lines)
      self.assertEqual(solution, 15)

  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()      
      
      solution = get_2th_solution(raw_lines)
      self.assertEqual(solution, 1134)

if __name__ == '__main__':
  unittest.main()