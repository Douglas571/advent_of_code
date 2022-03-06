from syntax_scoring import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day 10: Syntax Scoring ---')

    first_solution = get_1th_solution(raw_lines)
    print(f'1th part:\n  The total score is: {first_solution}')

    second_solution = get_2th_solution(raw_lines)
    print(f'2th part:\n  "your message": {second_solution}')    

if __name__ == '__main__':
  main()
