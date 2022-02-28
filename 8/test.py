import unittest
from seven_segment_search import *

class Test_Case(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      fods = extract_four_ouput_digits(f.readlines())
      self.assertEqual(fods[2], ["cg", "cg", "fdcagb", "cbg"])

      upns = count_unique_pattern_numbers(fods)
      self.assertEqual(upns, 26)

if __name__ == '__main__':
  unittest.main()