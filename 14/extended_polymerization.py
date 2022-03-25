import re
from collections import Counter
from collections import deque

TEMPLATE_RE = re.compile(r'[A-Z]{2,}')
PAIR_INSERTION_RE = re.compile(r'(?P<a>\w{2}) -> (?P<b>\w{1})')

def get_input(raw_lines):
  template = Counter()
  pair_ins = {}
  initial_ocurrencies = Counter()
  for l in raw_lines:
    if p := PAIR_INSERTION_RE.search(l):
      
      a = p.group('a')
      b = p.group('b')

      b1 = a[0] + b
      b2 = b + a[1]
      pair_ins[a] = (b1, b2, b)
      continue

    if t := TEMPLATE_RE.search(l):
      buff = [ c for c in l.strip('\n') ]

      for i in range(len(buff)):
        initial_ocurrencies[buff[i]] += 1

        if i == 0: continue

        token = buff[i-1] + buff[i]
        template[token] += 1

  return template, pair_ins, initial_ocurrencies

def print_input(t, pi):
  print()
  print(f'template: {t}')
  print(f'{len(pi)} pair insertions:')
  for i, p in enumerate(pi.items()):
    a, b = p
    print(f'  {i:2}. {a} -> {b}')
  print()

def get_1th_solution(raw_lines, steps=10):
  combinations, pair_ins, ocurrencies = get_input(raw_lines)
  # print_input(combinations, pair_ins)
  
    # take 1th part of template
    # get between insertions
    # add tuple of (index, insertions)
    # repeat until there's no more template chars

  for step in range(steps):
    # print(f'step {step+1}')

    new_comb = Counter()
    
    for k in combinations:
      v = combinations[k]
      if v > 0:
        combinations[k] = 0
        a, b, c = pair_ins[k]
        new_comb[a] += v
        new_comb[b] += v

        ocurrencies[c] += v
    # print(f'  old comb: {combinations}')    
    # print(f'  new comb: {new_comb}')
    # print(f'  ocurrencies: {ocurrencies}')
    combinations = new_comb
    # print(f'  result: {combinations}')    

  # print(f'ocurrencies: {ocurrencies}')
  c = ocurrencies
  sort = c.most_common()
  common = sort[0]
  un_common = sort[-1]

  # print(f'common={common}; un_common={un_common}')
  solution = common[1] - un_common[1]

  return solution

def run_step(mols, pair_ins):
  # print(f'before:{mols}')
  new_mols = Counter(mols)
  # print(f'after:{new_mols}')

  for m in mols:
    c = pair_ins[m]
    a = m[0]
    b = m[1]

    new_mols[m] -= 1
    A = a+c
    B = c+b
    new_mols[A] += 1
    new_mols[B] += 1

  return new_mols

def get_2th_solution(raw_lines):
  solution = get_1th_solution(raw_lines, steps=40)
  return solution
