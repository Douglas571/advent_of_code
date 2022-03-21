import re

TEMPLATE_RE = re.compile(r'\w{4,}')
PAIR_INSERTION_RE = re.compile(r'(?P<a>\w{2}) -> (?P<b>\w{1})')

def get_input(raw_lines):
  template = []
  pair_ins = []
  for l in raw_lines:

    if t := TEMPLATE_RE.search(l):
      template = [ c for c in l.strip('\n') ]

    if p := PAIR_INSERTION_RE.search(l):
      a = p.group('a')
      b = p.group('b')
      pair_ins.append((a, b))

  return template, pair_ins

def print_input(t, pi):
  print()
  print(f'template: {t}')
  print(f'{len(pi)} pair insertions:')
  for i, p in enumerate(pi):
    a, b = p
    print(f'  {i:2}. {a} -> {b}')
  print()

def get_1th_solution(raw_lines):
  template, pair_ins = get_input(raw_lines)
  print_input(template, pair_ins)
  


def get_2th_solution(raw_lines):
  pass
