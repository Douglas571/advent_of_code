import re
from collections import Counter

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

  while len(insertions) > 0:
    n, m = template.pop(0), insertions.pop(0)
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

def get_2th_solution(raw_lines):
  solution = get_1th_solution(raw_lines, 40)
  return solution
