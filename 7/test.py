import unittest
from the_treachery_of_whales import *

class Test_Case(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      horizontal_pos = get_horizontal_pos(f.readlines())
      self.assertEqual(horizontal_pos, [16,1,2,0,4,2,7,1,2,14])

      p, fuel = calc_cheapest_position(horizontal_pos)
      self.assertEqual(p, 2)
      self.assertEqual(fuel, 37)


if __name__ == '__main__':
  unittest.main()