import re

fold_re = re.compile(r'((?P<ax>\w)=(?P<amount>\d+?))')

def extract_fold(l):
  res = fold_re.search(l)
  ax = res.group('ax')
  amount = res.group('amount')

  return ax, amount

def get_input(raw_lines):
  gx = -1
  gy = -1
  
  dots = []
  folds = {
    'x': set(),
    'y': set()
  }
  c = 0
  for l in raw_lines:
    l = l.strip('\n')
    if l == '': continue

    if l[0] == 'f':
      ax, amount = extract_fold(l)
      amount = int(amount)
      folds[ax].add(amount)

      if c == 0:
        first_fold = (ax, amount)
        c += 1
      continue

    x, y = [ int(x) for x in l.split(',')]
    if gx < x: gx = x
    if gy < y: gy = y

    dots.append((x, y))

  return dots, folds, gx, gy, first_fold

def fold_x(m, x):
  new_m = []
  for row in m:
    new_row = []

    for i in range(x):
      j = -1 - i
      n = row[i] + row[j]
      new_row.append(n)

    new_m.append(new_row)

  return new_m

def fold_y(m, y):
  new_m = []

  for i in range(y):
    j = -1 - i
    # print(f'i={i}, j={j}')

    row_a = m[i]
    row_b = m[j]
    new_row = []
    for a, b in zip(row_a, row_b):
      new_row.append(a+b)

    new_m.append(new_row)

  return new_m

def print_m(m):
  for x in m:
    for y in x:
      if y == 0: print('.', end='')
      if y > 0: print('#', end='')
    print()

def get_paper(dots, gx, gy):
  m = [ [ 0 for x in range(gx+1) ] for y in range(gy+1)]
  for p in dots:
    x, y = p
    m[y][x] = 1
  return m

def get_total_dots(m):
  total_dots = 0
  for row in m:
    for d in row:
      if d != 0: total_dots += 1

  return total_dots

def get_1th_solution(raw_lines):
  dots, _, gx, gy, first_fold = get_input(raw_lines)
  m = get_paper(dots, gx, gy)

  ax, i = first_fold
  if ax == 'y':
    m = fold_y(m, i)
  else:
    m = fold_x(m, i)

  total_dots = get_total_dots(m)

  return total_dots

def get_2th_solution(raw_lines):
  dots, folds, gx, gy, _ = get_input(raw_lines)
  
  m = get_paper(dots, gx, gy)

  for y in folds['y']:
    # print(f'folding in y={y}')
    m = fold_y(m, y)
  
  for x in folds['x']:
    # print(f'folding in x={x}')
    m = fold_x(m, x)

  print_m(m)

  total_dots = get_total_dots(m)

  return total_dots
