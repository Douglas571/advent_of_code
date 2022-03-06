from smoke_basin import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()
    
    print('--- Day 9: Smoke Basin ---')

    solution = get_1th_solution(raw_lines)
    print(f'1t part:\n the sum of risk levels are: {solution}')

    second_solution = get_2th_solution(raw_lines)
    print(f'2t part:\n the product of largest basins are: {second_solution}')    

if __name__ == '__main__':
  main()