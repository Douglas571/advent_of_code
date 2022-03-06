def get_floor_map(raw_lines):
  m = []
  for line in raw_lines:
    new_line = [ int(n) for n in line.strip('\n')]
    m.append(new_line)

  return m

def is_lowest(m, i, j, checked=[]):
  n = m[i][j]
  c = 0
  low_p = n

  # check up
  if i-1 >= 0:
    new_n = m[i-1][j]
    if low_p >= new_n:
      c += 1
      low_p = new_n

  # check  rigth
  if j+1 < len(m[i]):
    new_n = m[i][j+1]
    if low_p >= new_n:
      c += 1
      low_p = new_n

  # check down
  if i+1 < len(m):
    new_n = m[i+1][j]
    if low_p >= new_n:
      c += 1
      low_p = new_n

  # check left
  if j-1 >= 0:
    new_n = m[i][j-1]
    if low_p >= new_n:
      c += 1
      low_p = new_n

  # print(f'FINAL: n={n}; low_p={low_p}; i={i}; j={j}')
  if low_p == n and c > 0:
    #print(f'c={c}')
    return False

  return low_p == n
  
def not_none(els):
  for e in els:
    if e == None:
      return False

  return True

def get_lowest_points(m):
  lowest_points = []
  checked_locations = [[ False for _ in range(len(m[0]))] for _ in range(len(m)) ]

  for i, row in enumerate(m):
    for j, n in enumerate(row):
      #if checked_locations[i][j]:
       # continue
      
      if is_lowest(m, i, j):
        #print(f'lowest: {n}')
        lowest_points.append(m[i][j])
      #print(f'New low: new_i={new_i}; new_j={new_j}')        

  return lowest_points
  # wrong guess 1815: too higth

def get_risk_levels(points):
  risk_levels = [ p + 1 for p in points]
  return risk_levels

def get_1th_solution(raw_lines):
  fm = get_floor_map(raw_lines)
  lwps = get_lowest_points(fm)
  rlvs = get_risk_levels(lwps)
  sum_rlvs = sum(rlvs)

  return sum_rlvs

def get_basins(m, i, j, checked_points=[]):
  points = []
  center = m[i][j]

  # directions
  UP    = (i-1, j)
  DOWN  = (i+1, j)
  RIGTH = (i, j+1)
  LEFT  = (i, j-1)

  if len(checked_points) == 0:
    checked_points = [[False for col in range(len(m[0]))] for row in range(len(m))]

  checked_points = checked_points.copy()

  points.append(center)
  checked_points[i][j] = True
  for r,c in [UP,RIGTH,DOWN,LEFT]:
    if (r >= 0 and r < len(m)) and (c >= 0 and c < len(m[r])):
      new_p = m[r][c]

      if checked_points[r][c] or new_p == 9:  continue

      sub_basins, checked_points = get_basins(m,r,c, checked_points)
      points.extend(sub_basins)

  return points, checked_points

def get_2th_solution(raw_lines):
  checked_points = []
  lowest_points = []
  all_basins = []
  m = get_floor_map(raw_lines)

  for i, row in enumerate(m):
    for j, n in enumerate(row):
      if is_lowest(m, i, j):
        lowest_points.append((i, j, m[i][j]))

  for i, j, n in lowest_points:
    basin, _ = get_basins(m, i, j)
    all_basins.append(len(basin))

  solution = 1
  all_basins = list(reversed(sorted(all_basins)))
  for b in all_basins[0:3]: solution *= b

  return solution
  # You guessed 712800, is to low.