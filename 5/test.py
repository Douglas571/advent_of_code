import unittest

class Test(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      pass

if __name__ == '__main__':
  unittest.main()