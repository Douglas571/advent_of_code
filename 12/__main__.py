from passage_pathing import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()

    print('--- Day 12: Passage Pathing ---')

    first_solution = get_1th_solution(raw_lines)
    print(f'1th part:\n\t"your message": {first_solution}')

    second_solution = get_2th_solution(raw_lines)
    print(f'2th part:\n\t"your message": {second_solution}')    

if __name__ == '__main__':
main()
