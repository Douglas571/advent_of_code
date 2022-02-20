def sonar_sweep(report):
  last_measure = None
  uppers = 0
  for msr in report:
    if last_measure and msr > last_measure:
      uppers += 1
    
    last_measure = msr

  return uppers

def are_enough_msr(total_msr, curr_msr_i, required):
  return total_msr - (curr_msr_i + 1) >= required

def windowed(report):
  windows = []
  total_measures = len(report)
  for i, msr in enumerate(report):

    if are_enough_msr(total_measures, i, 2):
      window = {
        'total': msr,
        'count': 1
      }

      windows.append(window)

    j = 1
    wl = len(windows)
    if i > wl:
      j = i - wl + 1

    while i - j >= 0 and windows[i-j]['count'] < 3:
      windows[i-j]['total'] += msr
      windows[i-j]['count'] += 1
      j += 1

  windowed_report = [ w['total'] for w in windows ]

  return windowed_report

def main():
  # for the second part
  with open('input2.txt') as f:
    report = [int(r) for r in f.readlines()]
    report = windowed(report)
    res = sonar_sweep(report)
    print(f'the upper measures are: {res}')

if __name__ == '__main__':
  main()