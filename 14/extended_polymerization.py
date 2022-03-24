import re
from collections import Counter
from collections import deque

TEMPLATE_RE = re.compile(r'\w{4,}')
PAIR_INSERTION_RE = re.compile(r'(?P<a>\w{2}) -> (?P<b>\w{1})')

def get_input(raw_lines):
  template = []
  pair_ins = {}
  for l in raw_lines:

    if t := TEMPLATE_RE.search(l):
      template = [ c for c in l.strip('\n') ]

    if p := PAIR_INSERTION_RE.search(l):
      
      a = p.group('a')
      b = p.group('b')
      pair_ins[a] = b

  return template, pair_ins

def print_input(t, pi):
  print()
  print(f'template: {t}')
  print(f'{len(pi)} pair insertions:')
  for i, p in enumerate(pi.items()):
    a, b = p
    print(f'  {i:2}. {a} -> {b}')
  print()

def make_insertions(insertions, template):
  new_template = []

  i = 0
  while len(insertions) > 0:
    n, m = template.pop(0) + insertions.pop(0)
    new_template.append(n)
    new_template.append(m)

  n = template.pop(0)
  new_template.append(n)

  return new_template

def get_1th_solution(raw_lines, steps=10):
  template, pair_ins = get_input(raw_lines)
  print_input(template, pair_ins)
  
    # take 1th part of template
    # get between insertions
    # add tuple of (index, insertions)
    # repeat until there's no more template chars

  for step in range(steps):
    print(f'step {step+1}')
    i = 1
    insertions = []
    while i < len(template):
      portion = template[i-1] + template[i]
      c = pair_ins[portion]
      insertions.append(c)
      i += 1

    new_template = make_insertions(insertions, template)
    # print(f'after step {step+1}: {new_template}')

    template = new_template

  c = Counter()
  for a in template:
    c[a] += 1
  print(c)

  sort = c.most_common()
  common = sort[0]
  un_common = sort[-1]

  print(f'common={common}; un_common={un_common}')
  solution = common[1] - un_common[1]

  return solution

def run_step(mols, pair_ins):
  print(f'before:{mols}')
  new_mols = Counter(mols)
  print(f'after:{new_mols}')

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
  template, pair_ins = get_input(raw_lines)

  mols = Counter()
  steps = 3

  # prepare the mols counter
  i = 1
  while i < len(template):
    m = template[i-1] + template[i]
    mols[m] += 1

    i += 1

  print(mols)

  for s in range(steps):
    mols = run_step(mols, pair_ins)
    print(mols)

  solution = 0
  return solution
