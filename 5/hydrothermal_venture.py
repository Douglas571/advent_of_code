def extract_segments(raw_data):
  sgms = []
  for line in raw_data:
    print(line)
    raw_p1, raw_p2 = line.split(' -> ')
    print(f'raw_p1: {raw_p1}')
    print(f'raw_p2: {raw_p2}')

    p1 = tuple(int(n) for n in raw_p1.split(','))
    p2 = tuple(int(n) for n in raw_p2.split(','))
    print(f'p1: {p1}')
    print(f'p2: {p2}')

    sgms.append((p1, p2))

  return sgms

def determine_lines_overlapes(segments):
  # just in case :v
  #sgms = segments.copy()

  diagrame = []
  lines_overlas = -1

  # a sgm is a list like this: [[x1, y1], [x2, y2]]

  for sgm in segments:
    pass

  return lines_overlas


if __name__ == '__main__':
  main()