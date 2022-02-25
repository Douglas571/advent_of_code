import unittest
from hydrothermal_venture import *

class Test(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      raw_data = f.readlines()
      segments, hx, hy = extract_segments(raw_data)

      self.assertEqual(len(segments), 10)
      self.assertEqual(segments[0][0], (0, 9))
      self.assertEqual(segments[0][1], (5, 9))
      #7,0 -> 7,4
      self.assertEqual(segments[4][0], (7, 0))
      self.assertEqual(segments[4][1], (7, 4))
      #5,5 -> 8,2
      self.assertEqual(segments[-1][0], (5, 5))
      self.assertEqual(segments[-1][1], (8, 2))

      dangerours_points = determine_lines_overlapes(segments, hx, hy)
      self.assertEqual(dangerours_points, 5)

  def test_two(self):
    with open('example2.txt') as f:
      raw_data = f.readlines()
      segments, hx, hy = extract_segments(raw_data)

      dangerours_points = determine_lines_overlapes(segments, hx, hy)
      self.assertEqual(dangerours_points, 10)      

if __name__ == '__main__':
  unittest.main()