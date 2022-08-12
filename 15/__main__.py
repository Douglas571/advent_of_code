import time
import math
from chiton import *

def timeit(fn):
  start = time.time()
  res = fn()
  end = time.time()
  total_time = end - start

  return res, total_time

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day 15: Chiton ---')

    ### first part ###
    first_solution, t_time = timeit(lambda: get_1th_solution(raw_lines))
    first_solution = f'{first_solution:,}'
    msg = 'your message'
    print('1th part:\n  %s: %s; in %4.2fsec'%(msg, first_solution, t_time))
    print()

    ### second part ###
    sec_solution, t_time = timeit(lambda: get_2th_solution(raw_lines))
    sec_solution = f'{second_solution:,}'
    msg = 'your message'
    print('2th part:\n  %s: %s; in %4.2fsec'%(msg, sec_solution, t_time))    
    print()

if __name__ == '__main__':
  main()
