from collections import Counter

def extract_four_ouput_digits(raw_lines):
  fods = []

  for line in raw_lines:
    fods.append(line.strip('\n').split(' | ')[1].split(' '))

  return fods

def count_unique_pattern_numbers(rows_of_digits):
  count = 0

  for row in rows_of_digits:
    for d in row:
        if len(d) in [2, 3, 4, 7]:
          count += 1

  return count 

def main():
  with open('input.txt') as f:
    fods = extract_four_ouput_digits(f.readlines())
    upn = count_unique_pattern_numbers(fods)
    print('--- Seven Segment Search ---')
    print('1th part:')
    print(f'the numbs of unique patters are: {upn}')

if __name__ == '__main__':
  main()