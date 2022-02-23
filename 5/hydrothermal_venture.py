def extract_segments(raw_data):
  sgms = []
  for line in raw_data:
    raw_p1, raw_p2 = line.split(' -> ')

    p1 = tuple(int(n) for n in raw_p1.split(','))
    p2 = tuple(int(n) for n in raw_p2.split(','))

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