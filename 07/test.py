import unittest
from the_treachery_of_whales import *

class Test_Case(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      horizontal_pos = get_crabs_groups(f.readlines())
      self.assertEqual(horizontal_pos['1'], 2)

      p, fuel = calc_cheapest_position(horizontal_pos)
      self.assertEqual(p, 2)
      self.assertEqual(fuel, 37)

  def test_two(self):
    with open('example.txt') as f:
      print()
      horizontal_pos = get_crabs_groups(f.readlines())
      self.assertEqual(horizontal_pos['1'], 2)

      p, fuel = calc_cheapest_position(horizontal_pos, two='True')
      self.assertEqual(p, 5)
      self.assertEqual(fuel, 168)


if __name__ == '__main__':
  unittest.main()