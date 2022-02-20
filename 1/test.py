import unittest
from sonar_sweep import *

class TestStringMethods(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      report = [int(r) for r in f.readlines()]
      res = sonar_sweep(report)

      self.assertEqual(7, res)

      windowed_report = windowed(report)

      w_exp = [607, 618, 618, 617, 647, 716, 769, 792]
      self.assertEqual(w_exp, windowed_report)
      res = sonar_sweep(windowed_report)

      self.assertEqual(5, res)

if __name__ == '__main__':
  unittest.main()