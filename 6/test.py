import unittest
from lanternfish import *

class Test_Case(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      fido = get_fishes_day_one(f.readlines())

      self.assertEqual(fido, [3,4,3,1,2])

      grow_after_day = calc_fish_grow_per_day(fido)

      self.assertEqual(grow_after_day[18], 26)
      self.assertEqual(grow_after_day[80], 5934)

      grow_in_day = calc_fish_grow_per_day(fido, limit=256)
      self.assertEqual(grow_in_day[256], 26984457539)

if __name__ == '__main__':
  unittest.main()