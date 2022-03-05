from smoke_basin import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()
  
    solution = get_1th_solution(raw_lines)

    print('--- Day 9: Smoke Basin ---')
    print(f'1t part\n the sum of risk levels are: {solution}')

if __name__ == '__main__':
  main()