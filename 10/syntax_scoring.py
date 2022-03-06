from collections import deque

def get_input(raw_lines):
  return [ deque(ln) for ln in raw_lines ]

OPSIDE = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">" 
}

def analise(char, line):
  # print(f'line={line}')

  next_char = '\n'
  if len(line) > 0:
    next_char = line.popleft()
    

  # print(f'char={char}, next_char={next_char}')
  if OPSIDE[char] == next_char:
    # print(f'block={char}...{next_char}')
    return None, line

  if next_char in OPSIDE.keys():
    # print('into')
    err, line = analise(next_char, line)
    # print(f'out: char={char},err={err}')

    if err:
      return err, line

    return analise(char, line)

  err = next_char
  return err, line

def check(lines):
  errors_found = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0 
  }

  for ln in lines:
    char = ln.popleft()
    err, _ = analise(char, ln)
    if err and err != '\n':
      # print(f'SYNTAX ERROR: {err}')
      errors_found[err] += 1

  return errors_found

SCORES = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

def get_1th_solution(raw_lines):
  score = 0
  lines = get_input(raw_lines)
  # corrupted_lines = get_corrupted_lines(raw_lines)
  errors_found = check(lines)

  for char, count in errors_found.items():
    score += SCORES[char] * count

  return score

def get_2th_solution(raw_lines):
  pass
