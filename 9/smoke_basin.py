def get_floor_map(raw_lines):
  m = []
  for line in raw_lines:
    new_line = [ int(n) for n in line.strip('\n')]
    m.append(new_line)

  return m

def get_lowest_point(m, i, j, checked=[]):
  new_i, new_j = i, j
  original_n = m[i][j]
  n = original_n
  checked = checked.copy()

  # check up
  if i-1 >= 0:
    new_n = m[i-1][j]
    if n > new_n:
      n = new_n
      new_i, new_j = i-1, j

  # check  rigth
  if j+1 < len(m[i]):
    new_n = m[i][j+1]
    if n > new_n:
      new_i, new_j = i, j+1
      n = new_n

  # check down
  if i+1 < len(m):
    new_n = m[i+1][j]
    if n > new_n:
      new_i, new_j = i+1, j
      n = new_n

  # check left
  if j-1 >= 0:
    new_n = m[i][j-1]
    if n > new_n:
      new_i, new_j = i, j-1
      n = new_n

  if original_n != n:
    #print(f'original_n={original_n}; n={n}; new_i={new_i}; new_j={new_j}')
    return get_lowest_point(m, new_i, new_j, checked=checked)

  #print(f'FINAL: original_n={original_n}; n={n}; new_i={new_i}; new_j={new_j}')
  if checked[i][j]:
    return None, None, checked
  
  checked[i][j] = True
  return new_i, new_j, checked


  
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
      if checked_locations[i][j]:
        continue
      
      new_i, new_j, checked_locations = get_lowest_point(m, i, j, checked=checked_locations)

      #print(f'New low: new_i={new_i}; new_j={new_j}')
      if not_none([new_i,new_j]):
        lowest_points.append(m[new_i][new_j])

  return sorted(lowest_points)
  # wrong guess 1815: so higth

def get_risk_levels(points):
  risk_levels = [ p + 1 for p in points]
  return risk_levels