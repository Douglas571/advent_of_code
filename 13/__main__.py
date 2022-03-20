import time
import math
from transparent_origami import *

def timeit(fn):
  start = time.time()
  res = fn()
  end = time.time()
  total_time = end - start

  return res, total_time

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day 13: Transparent Origami ---')

    ### first part ###
    first_solution, t_time = timeit(lambda: get_1th_solution(raw_lines))
    msg = 'The total dots are'
    print('1th part:\n\t%s: %s; in %4.2fsec'%(msg, first_solution, t_time))

    ### second part ###
    (second_solution, code), t_time = timeit(lambda: get_2th_solution(raw_lines))
    msg = 'The total dots are'
    print('2th part:\n\t%s: %s; in %4.2fsec'%(msg, second_solution, t_time))    
    print('\tThe code is:')
    print_m(code)

if __name__ == '__main__':
  main()
