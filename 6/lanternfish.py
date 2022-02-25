def get_fishes_day_one(raw_lines):
  fido = [ int(n) for n in raw_lines[0].split(',')]
  return fido

def calc_fish_grow_per_day(fishes_in_day_one, limit=80):
  grow_in_day = [fishes_in_day_one.copy(),]

  for _ in range(limit):
    new_day = []
    new_fishes = 0

    for n in grow_in_day[-1]:
      if n == 0:
        new_n = 6
        new_fishes += 1

      if n > 0:
        new_n = n - 1

      new_day.append(new_n)

    for _ in range(new_fishes):
      new_day.append(8)

    grow_in_day.append(new_day)

  return [ len(fishes) for fishes in grow_in_day ]

def main():
  with open('input.txt') as f:
    fido = get_fishes_day_one(f.readlines())

    print('--- Lanternfish ---')
    fishes_per_day = calc_fish_grow_per_day(fido)

    print(f'After day 80 are: {fishes_per_day[80]} fishes')

if __name__ == '__main__':
  main()