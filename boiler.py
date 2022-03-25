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
main_file = ('__main__.py', f"""import time
import math
from {lib_name} import *

def timeit(fn):
  start = time.time()
  res = fn()
  end = time.time()
  total_time = end - start

  return res, total_time

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day {day}: {name} ---')

    ### first part ###
    first_solution, t_time = timeit(lambda: get_1th_solution(raw_lines))
    first_solution = f'{first_solution:,}'
    msg = 'your message'
    print('1th part:\n  %s: %s; in %4.2fsec'%(msg, first_solution, t_time))
    print()

    ### second part ###
    sec_solution, t_time = timeit(lambda: get_2th_solution(raw_lines))
    sec_solution = f'{sec_solution:,}'
    msg = 'your message'
    print('2th part:\n  %s: %s; in %4.2fsec'%(msg, sec_solution, t_time))    
    print()

if __name__ == '__main__':
  main()
""")

lib_file = (f'{lib_name}.py', f"""def get_input(raw_lines):
  pass

def get_1th_solution(raw_lines):
  pass

def get_2th_solution(raw_lines):
  pass
""")

test_file = ('test.py', f"""import unittest
from {lib_name} import *

class Test_Case(unittest.TestCase):
  #@unittest.skip
  def test_one(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      solution = get_1th_solution(raw_lines)
      # self.assertEqual(solution, 0000)

  #@unittest.skip
  def test_two(self):
    with open('example.txt') as f:
      raw_lines = f.readlines()

      # solution = get_2th_solution(raw_lines)
      # self.assertEqual(solution, 0000)

if __name__ == '__main__':
  unittest.main()""")

files = [
  main_file, 
  lib_file, 
  test_file, 
  ('input.txt', None), 
  ('example.txt', None), 
  ('puzzle.txt', None)]

folder = f'{cwd}/{day}'

if not os.path.exists(folder):
  os.mkdir(folder)

for name, content in files:
  with open(f'{folder}/{name}', 'w') as f:
    if content:
      f.write(content)