from collections import deque
from enum import Enum
import math

def get_input(raw_lines):
  return [ deque(ln) for ln in raw_lines ]

class States(Enum):
  CORRUPTED = 0
  GOOD = 1
  INCOMPLETED = 2 

OPSIDE = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">" 
}

SCORES = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

FIX_SCORES = {
  ")": 1,
  "]": 2,
  "}": 3,
  ">": 4
}

def get_input(raw_lines):
  input_data = [ ln.strip('\n') for ln in raw_lines ]
  return input_data

def check_ln(ln, char=None, payload=None):
  payload = payload or []
  char = char or ln.popleft()

  if len(ln) == 0: 
    payload.append(OPSIDE[char])
    return States.INCOMPLETED, payload
  
  next_char = ln.popleft()

  if next_char == OPSIDE[char]:
    return States.GOOD, None

  if not next_char in OPSIDE.keys():
    return States.CORRUPTED, next_char

  sub_state, payload = check_ln(ln, next_char, payload)

  if sub_state == States.INCOMPLETED:
    payload.append(OPSIDE[char])
    return States.INCOMPLETED, payload

  if sub_state == States.CORRUPTED:
    return States.CORRUPTED, payload
  
  return check_ln(ln, char, payload)  

def check(lines):
  corrupted_lines = []
  incompleted_lines = []
  complements = []
  errors_found = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0 
  }
  
  for ln in lines:
    ln_copy = deque(ln)

    state, payload = check_ln(ln_copy)
    while state == States.GOOD and len(ln_copy) > 0:
      state, payload = check_ln(ln_copy)

    match(state):
      case States.INCOMPLETED:  
        incompleted_lines.append(ln)
        payload = str().join(payload)
        complements.append(payload)
    
      case States.CORRUPTED:
        corrupted_lines.append(ln)
        errors_found[payload] += 1

  return corrupted_lines, errors_found, incompleted_lines, complements

def get_1th_solution(raw_lines):
  score = 0
  lines = get_input(raw_lines)
  corrupted_lines, errors_found, _, _ = check(lines)

  for char, count in errors_found.items():
    score += SCORES[char] * count

  return score


def get_2th_solution(raw_lines):
  solution = 0

  lines = get_input(raw_lines)
  _, _, incompleted_lines, complements = check(lines)

  scores = []

  for compl in complements:
    scr = 0
    for char in compl:
      scr = (scr * 5) + FIX_SCORES[char]

    scores.append(scr)

  middle = math.floor(len(scores) / 2)
  solution = sorted(scores)[middle]
  return solution
