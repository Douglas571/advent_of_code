def get_fishes_day_one(raw_lines):
  fido = [ int(n) for n in raw_lines[0].split(',')]
  return fido

def calc_total_linternfishes(groups):
  count = 0
  for g in groups:
    count += g['count']
  return count

def calc_fish_grow_per_day(fishes_in_day_one, limit=80):
  grow_in_day = [{"clock": i, "count": 0} for i in range(9)]
  total_fishes_per_day = []
  
  for n in fishes_in_day_one:
    grow_in_day[n]["count"] += 1

  c = calc_total_linternfishes(grow_in_day)
  total_fishes_per_day.append(c)

  for day in range(limit):
    print(f'day {day}')
    new_borns = 0
    for i, group in enumerate(grow_in_day):
      if i == 0:
        new_borns = group['count']
        continue

      grow_in_day[i-1]['count'] = group['count']

      if i == 7:
        grow_in_day[i-1]['count'] += new_borns 

    grow_in_day[8]['count'] = new_borns

    count = calc_total_linternfishes(grow_in_day)
    total_fishes_per_day.append(count)

  return total_fishes_per_day

def main():
  with open('input.txt') as f:
    fido = get_fishes_day_one(f.readlines())

    print('--- Lanternfish ---')
    fishes_after_day = calc_fish_grow_per_day(fido, limit=256)

    print('1th part:')
    print(f'After day 80 are: {fishes_after_day[80]} fishes')
    print('2th part:')
    print(f'After day 256 are: {fishes_after_day[256]} fishes')

if __name__ == '__main__':
  main()