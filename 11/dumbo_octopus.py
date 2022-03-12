from collections import deque

# Constants...
def get_directions(i, j):
  up = (i-1, j)
  down = (i+1, j)
  rigth = (i, j+1)
  left = (i, j-1)
  left_up = (i-1, j-1)
  left_down = (i+1, j-1)
  rigth_up = (i-1, j+1)
  rigth_down = (i+1, j+1)

  directions = (
    up, rigth_up, rigth, rigth_down, 
    down, left_down, left, left_up
  )

  return directions

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
      if n == 0:
        print('.', end=' ')
        continue
      print(n, end=' ')
    print()

def m_copy(m):
  return [ l.copy() for l in m ]

def run_step(M):
  m = m_copy(M)
  flashed = [[None]*len(r) for r in m]
  flashes = 0

  for i, row in enumerate(M):
    for j, el in enumerate(row):
      if el == ' ': continue
      m[i][j] += 1

  # print('before eny flash:')
  # print_m(m)

  keep_run = True
  while keep_run:
    keep_run = False
    for r, row in enumerate(m):
      for c, el in enumerate(row):
        if el == ' ': continue

        if m[r][c] > 9:
          flashed[r][c] = True
          flashes += 1
          keep_run = True

          directions = get_directions(r, c)
          for i, j in directions:
            if m[i][j] == ' ': continue
            m[i][j] += 1
        
        if flashed[r][c]:
          m[r][c] = 0        

  return m, flashes

def get_1th_solution(raw_lines):
  steps = 100
  solution = 0
  m = get_input(raw_lines)
  # print_m(m, '1th iter')

  flashes = 0
  for stp in range(steps):
    m, f = run_step(m)
    flashes += f
    # print(f'after step {(stp+1)}: {f} flashes')
    # print_m(m)

  solution = flashes
  return solution

def get_2th_solution(raw_lines):
  solution = 0
  m = get_input(raw_lines)
  step = 0

  while solution == 0:
    total = 0
    step += 1
    m, f = run_step(m)

    for row in m:
      for n in row:
        if n != ' ': total += n

    if total == 0:
      solution = step
      break

    # print(f'after step {(stp+1)}: {f} flashes')
    # print_m(m)

  return solution  
