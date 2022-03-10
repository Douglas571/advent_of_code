from collections import deque

def get_input(raw_lines):
  f = ' '
  m = []
  m.append([ f for _ in range(12) ])
  for l in raw_lines:
    row = []
    row.append(f)
    row.extend([ int(n) for n in l.strip("\n")])
    row.append(f)

    m.append(row)

  m.append([ f for _ in range(12) ])

  # m = [ [ int(n) for n in l.strip('\n') ] for l in raw_lines ]
  return m

def print_m(m, msg=None):
  if msg: print(f'  --- {msg} ---')

  for r in m:
    for n in r:
      print(n, end=' ')
    print()

def m_copy(m):
  return [ l.copy() for l in m ]

def run_step(M):
  flashes = 0
  m = m_copy(M)
  next_m = m_copy(m)

  to_flash = deque()

  for i, l in enumerate(m):
    for j, n in enumerate(l):
      if next_m[i][j] == ' ': continue

      next_m[i][j] += 1

      if next_m[i][j] >= 9:
        to_flash.append((i, j))

  to_flash_2 = deque()

  while len(to_flash) > 0:
    i, j = to_flash.popleft()
    next_m[i][j] = 0

    if next_m[i -1][j] != ' ':
      next_m[i -1][j] += 1


    if next_m[i -1][j -1] != ' ':
      next_m[i -1][j -1] += 1

    if next_m[i][j -1] != ' ':
      next_m[i][j -1] += 1

    if next_m[i +1][j -1] != ' ':
      next_m[i +1][j -1] += 1

    if next_m[i +1][j] != ' ':
      next_m[i +1][j] += 1

    if next_m[i +1][j +1] != ' ':
      next_m[i +1][j +1] += 1

    if next_m[i][j +1] != ' ':
      next_m[i][j +1] += 1


  for i, l in enumerate(m):
    for j, n in enumerate(l):
      if next_m[i][j] != ' ':
        next_m[i][j] += 1  

  print_m(next_m, 'bucle i')

  return flashes, next_m

def get_1th_solution(raw_lines):
  steps = 100
  solution = 0
  m = get_input(raw_lines)
  print_m(m, '1th iter')

  flashes = 0
  for s in range(100):
    f, m = run_step(m)
    flashes += f

  print(f)
  return solution

def get_2th_solution(raw_lines):
  pass
