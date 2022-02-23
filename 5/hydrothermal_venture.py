def extract_segments(raw_data):
  sgms = []
  hx = 0
  hy = 0
  for line in raw_data:
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

def determine_lines_overlapes(segments, hx, hy):
  diagrame = [[ 0 for _ in range(hx + 1)] for _ in range(hy + 1)]
  lines_overlaps = -1

  # a sgm is a list like this: ((x1, y1), (x2, y2))
  for sgm in segments:
    p1, p2 = sgm
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    if x1 is x2:
      #print('vertical')
      start = min([y1, y2])
      end = max([y1, y2]) + 1
      
      for y in range(start, end):
        diagrame[y][x1] += 1
      continue

    if y1 is y2:
      #print('horizontal')
      start = min([x1, x2])
      end = max([x1, x2]) + 1
      
      for x in range(start, end):
        diagrame[y1][x] += 1
      continue

  lines_overlaps = count_overlapes(diagrame)

  return lines_overlaps

def main():
  with open('input.txt') as f:
    raw_data = f.readlines()
    segments, hx, hy = extract_segments(raw_data)

    dangerours_points = determine_lines_overlapes(segments, hx, hy)
    print(f'Dangerous points: {dangerours_points}')

if __name__ == '__main__':
  main()