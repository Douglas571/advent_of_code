from collections import deque
from enum import Enum
import math

def get_input(raw_lines):
  return [ deque(ln) for ln in raw_lines ]

OPSIDE = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">" 
}

def analise(char, line, rest=[]):
  # print(f'line={line}')

  rest = rest.copy()

  next_char = '\n'
  if len(line) > 0:
    next_char = line.popleft()
    

  #print(f'char={char}, next_char={next_char}')
  if OPSIDE[char] == next_char:
    # print(f'block={char}...{next_char}')
    return None, line, rest

  if next_char in OPSIDE.keys():
    #print('into')
    err, line, rest = analise(next_char, line, rest)
    #print(f'out: char={char},err={err}, rest={rest}')

    if len(rest) > 0:
      rest.append(OPSIDE[char])

    if err:
      return err, line, rest

    #print('reanalize')
    return analise(char, line, rest)

  rest.append(OPSIDE[char])
  #print(f'rest={rest}')

  err = next_char
  return err, line, rest

def check(lines):
  # print('\n--- checking ---')
  completations = []
  errors_found = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0 
  }

  for ln in lines:
    #print('iter')
    # print(', '.join(ln))
    char = ln.popleft()
    err, _, rest = analise(char, ln)
    # print(f'err={err}')

    if err:
      if err != '\n':
        # print(f'SYNTAX ERROR: {err}')
        # print('corrupta')
        errors_found[err] += 1
        continue
      
      # print(f'FINAL: rest = {rest}')
      completations.append(rest)

      
    

  return errors_found, completations

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
  errors_found, _ = check(lines)

  for char, count in errors_found.items():
    score += SCORES[char] * count

  return score

# V2

FIX_SCORES = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

class States(Enum):
  CORRUPTED = 0
  GOOD = 1
  INCOMPLETED = 2 

def get_input_2(raw_lines):
  input_data = [ ln.strip('\n') for ln in raw_lines ]
  return input_data

def check_ln(ln, char=None, rest=None):
  if not rest:
    rest = []

  print(f'init checking')
  char = char or ln.popleft()
  print(f'  char={char}')

  if len(ln) == 0: 
    print('thers no more chars! incompleted')
    rest.append(OPSIDE[char])
    return States.INCOMPLETED, rest
  

  next_char = ln.popleft()
  print(f'  next_char={next_char}')
  print(ln)

  if next_char == OPSIDE[char]:
    print(f'block: {char}...{next_char}')
    return States.GOOD, None

  if next_char in OPSIDE.keys():
    state, rest = check_ln(ln, next_char, rest)
    if state == States.INCOMPLETED:
      rest.append(OPSIDE[char])
      return state, rest

    if state == States.GOOD:

      return check_ln(ln, char, rest)

    return state, rest

  return States.CORRUPTED, None

"""
def check_ln_2(ln):
  chars = deque(ln)
  st = None

  while len(chars):
    char = chars.popleft()
    next_char = chars.popleft()

    if next_char == OPSIDE[char]:
      st = States.GOOD

    if 
"""

def get_incompleted_lines(lines):
  print('--- get_incompleted_lines() ---')
  incompleted_lines = []
  complements = []
  
  for i, ln in enumerate(lines):
    ln_copy = deque(ln)

    state, rest = check_ln(ln_copy)
    while state == States.GOOD and len(ln_copy) > 0:
      print('REPEAT')
      state, rest = check_ln(ln_copy)

    if state == States.INCOMPLETED:
      print(f'{i}.INCOMPLETED line:')
      print(f'  {ln}')
      print(f'  rest={rest}')

      incompleted_lines.append(ln)
      rest = str().join(rest)
      complements.append(rest)
      continue

    print(f'{i}.CORUPTED line:')
    print(f'  {ln}')


  
  print(f'incompleted lines={len(incompleted_lines)}')
  return incompleted_lines, complements

def fix_line(line):
  ln_copy = line()
  fix = []

  return fix

def get_2th_solution(raw_lines):
  solution = 0

  lines = get_input_2(raw_lines)
  incompleted_lines, complements = get_incompleted_lines(lines)

  print(complements)
  scores = []

  for compl in complements:
    scr = 0
    for char in compl:
      scr *= 5
      scr += FIX_SCORES[char]

    scores.append(scr)

  scores = sorted(scores)
  print(scores)
  middle = math.floor(len(scores) / 2)
  solution = scores[middle]
  return solution
