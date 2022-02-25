def extract_segments(raw_data):
  sgms = []
  hx = 0
  hy = 0
  for line in raw_data:
    if len(line.strip()) == 0: continue

    raw_p1, raw_p2 = line.split(' -> ')

    p1 = tuple(int(n) for n in raw_p1.split(','))
    p2 = tuple(int(n) for n in raw_p2.split(','))

    x_max = max((p1[0], p2[0]))
    y_max = max((p1[1], p2[1]))

    if x_max > hx:
      hx = x_max

    if y_max > hy:
      hy = y_max

    sgms.append((p1, p2))

  return sgms, hx, hy

def print_d(diagrame):

  """
    Should print a diagram like this:
    .......1..
    ..1....1..
    ..1....1..
    .......1..
    .112111211
    ..........
    ..........
    ..........
    ..........
    222111....
  """
  print()
  for row in diagrame:
    for n in row:
      if n == 0: 
        print('.', end=' ')
        continue
      print(n, end=' ')
    print()

def count_overlapes(diagrame):
  c = 0
  for row in diagrame:
    for n in row:
      if n >= 2: c += 1

  return c

def horizontal_line(dgrm, x, y1, y2):
  start = min(y1, y2)
  end = max(y1, y2) + 1
  
  for y in range(start, end):
    dgrm[y][x] += 1

def vertical_line(dgrm, y, x1, x2):
  start = min(x1, x2)
  end = max(x1, x2) + 1
  
  for x in range(start, end):
    dgrm[y][x] += 1

def diagonal_line(dgrm, x1, x2, y1, y2):
  distance = abs(x1 - x2)

  if y1 < y2: v = 1 
  else: v = -1

  if x1 < x2: h = 1 
  else: h = -1

  for _ in range(distance + 1):
    dgrm[y1][x1] += 1
    y1 += v
    x1 += h

def determine_lines_overlapes(segments, hx, hy, diagonal=False):
  diagrame = [[ 0 for _ in range(hx + 1)] for _ in range(hy + 1)]
  lines_overlaps = -1

  # a sgm is a list like this: ((x1, y1), (x2, y2))
  for sgm in segments:
    (x1, y1), (x2, y2) = sgm

    if x1 == x2:
      horizontal_line(diagrame, x1, y1, y2)
      continue

    if y1 == y2:
      vertical_line(diagrame, y1, x1, x2)
      continue

    if diagonal:
      diagonal_line(diagrame, x1, x2, y1, y2)

  lines_overlaps = count_overlapes(diagrame)

  return lines_overlaps

def main():
  with open('input.txt') as f:
    raw_data = f.readlines()
    segments, hx, hy = extract_segments(raw_data)

    print('--- Hydrothermal Venture ---')

    print('1th part:')
    dangerours_points = determine_lines_overlapes(segments, hx, hy)
    print(f'Dangerous points: {dangerours_points}')

    print('2th part:')
    dangerours_points = determine_lines_overlapes(segments, hx, hy, diagonal=True)
    print(f'Dangerous points (with diagonal): {dangerours_points}')

if __name__ == '__main__':
  main()