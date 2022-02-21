import unittest
from dive import *

class TestStringMethods(unittest.TestCase):
  def test_one(self):
    with open('example.txt') as f:
      commands = []
      for raw in f.readlines():
        name, amount = raw.split(' ')
        cmd = Command(name, amount)
        commands.append(cmd)

      hp, d = calc_course(commands)
      self.assertEqual(150, (d*hp))

  def test_part_2(self):
    with open('example.txt') as f:
      commands = []
      for raw in f.readlines():
        name, amount = raw.split(' ')
        cmd = Command(name, amount)
        commands.append(cmd)

      hp, d = calc_course_2(commands)
      self.assertEqual(15, hp)
      self.assertEqual(60, d)
      
if __name__ == '__main__':
  unittest.main()