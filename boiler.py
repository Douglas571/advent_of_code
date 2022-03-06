import sys
import json
import os

day = sys.argv[1]
name = sys.argv[2]
cwd = os.getcwd()

def to_camel_case(name):
  s = name.lower().replace(' ', '_')
  return s

solution_p = '{first_solution}'
solution_2_p = '{second_solution}'

lib_name = to_camel_case(name)
main_file = ('__main__.py', f"""from {lib_name} import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day {day}: {name} ---')

    first_solution = get_1th_solution(raw_lines)
    print(f'1th part:\\n\\t"your message": {solution_p}')

    second_solution = get_2th_solution(raw_lines)
    print(f'2th part:\\n\\t"your message": {solution_2_p}')    

if __name__ == '__main__':
main()
""")

lib_file = (f'{lib_name}.py', f"""def get_input(raw_line):
  pass

def get_1th_solution(raw_lines):
  pass

def get_2th_solution(raw_lines):
  pass
""")

test_file = ('test.py', f"""import unittest
from smoke_basin import *

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()      

  #@unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

if __name__ == '__main__':
  unittest.main()""")

files = [main_file, lib_file, test_file]

for name, content in files:
  with open(f'{cwd}/{day}/{name}', 'w') as f:
    f.write(content)