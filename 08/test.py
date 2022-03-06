import unittest
from seven_segment_search import *

class Test_Case(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      data = extrat_digits(f.readlines())
      #self.assertEqual(data[2]["output"], ["cg", "cg", "fdcagb", "cbg"])

      fods = get_four_output_digits(data)
      upns = count_unique_pattern_numbers(fods)
      self.assertEqual(upns, 26)

  def test_decoder(self):
    exp_digits = {
      "abcdefg": "8",
      "abd": "7",
      "abef": "4",
      "ab": "1",
      "bcdef": "5",
      "acdfg": "2",
      "abcdf": "3",
      "abcdef": "9",
      "bcdefg": "6",
      "abcdeg": "0",
    }


    with open('base-example.txt') as f:
      digits = extrat_digits(f.readlines())
      entry = digits[0]

      #self.assertEqual(entry['output'], ["cdfeb", "fcadb", "cdfeb", "cdbaf"])
      self.assertEqual(entry['input'][-1], "ab")

      res = decode_digits(digits)
      self.assertEqual(len(res), 1)
      self.assertEqual(exp_digits, res[0]['decoded_digits'])
      self.assertEqual(res[0]['output_v'], "5353")

  def test_three(self):
    with open('example.txt') as f:
      digits = extrat_digits(f.readlines())

      res = decode_digits(digits)
      self.assertEqual(res[3]['output_v'], "9361")
      self.assertEqual(res[-1]['output_v'], "4315")


if __name__ == '__main__':
  unittest.main()