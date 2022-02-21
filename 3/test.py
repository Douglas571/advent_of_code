import unittest
from binary_diagnostic import *

class TestStringMethods(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      measures = f.readlines()
      measures = [ msr.strip() for msr in measures]
      gamma_rate, epsilon_rate = binary_diagnostic(measures)

      self.assertEqual(22, gamma_rate)
      self.assertEqual(9, epsilon_rate)

  def test_part_2(self):
    with open('example.txt') as f:
      measures = f.readlines()
      measures = [ msr.strip() for msr in measures]
      (
        oxygen_generator_rating, 
        co2_scrubber_rate
      ) = binary_diagnostic_2(measures)

      self.assertEqual(23, oxygen_generator_rating)
      self.assertEqual(10, co2_scrubber_rate)
      
if __name__ == '__main__':
  unittest.main()