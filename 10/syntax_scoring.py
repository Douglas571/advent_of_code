from collections import deque

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
  print('\n--- checking ---')
  completations = []
  errors_found = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0 
  }

  for ln in lines:
    print('iter')
    print(', '.join(ln))
    char = ln.popleft()
    err, _, rest = analise(char, ln)
    print(f'err={err}')

    if err:
      if err != '\n':
        # print(f'SYNTAX ERROR: {err}')
        print('corrupta')
        errors_found[err] += 1
        continue
      
      print(f'FINAL: rest = {rest}')
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

FIX_SCORES = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

def get_2th_solution(raw_lines):
  solution = 0

  lines = get_input(raw_lines)
  _, completations = check(lines)

  scores = []
  for compl in completations:
    scr = 0
    for char in compl:
      scr *= 5
      scr += FIX_SCORES[char]
    scores.append(scr)

  print(sorted(scores))


  return solution
