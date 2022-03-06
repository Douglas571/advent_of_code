from collections import Counter

def get_crabs_groups(raw_lines):
  crabs_groups = Counter()
  hp = [int(n) for n in raw_lines[0].split(',')]

  for p in hp:
    crabs_groups[str(p)] += 1

  return crabs_groups

def calc_cheapest_position(crabs_groups, two=False):  
  better_p = [0, 0]

  positions = []

  total = [ int(p) for p, _ in crabs_groups.items()]
  start = min(total)
  end = max(total) + 1
  for position in range(start, end):
    print(position)
    movements = {
      'total_fuel': 0,
      'moves': []
    }

    for p, c in crabs_groups.items():
      move = {}

      move['start'] = int(p)

      if two:
        fuel = 0
        steps = abs(int(p) - position)
        for i in range(1, steps + 1):
          fuel += i
        move['fuel'] = fuel * c

      else:
        move['fuel'] = abs(int(p) - position) * c



      movements['moves'].append(move)
      movements['total_fuel'] += move['fuel']

    positions.append(movements)

  better_p[1] = positions[0]['total_fuel']
  for p, movements in enumerate(positions):
    fuel = movements['total_fuel']

    tf = movements['total_fuel']
    #print(f'{p}.{tf}')
    if fuel < better_p[1]:
      better_p = (p, fuel)
  
  return better_p
  #wrogn = 336721

def main():
  with open('input.txt') as f:
    print('--- The Treachery of Whales ---')
    print('1th part:')

    cgs = get_crabs_groups(f.readlines())
    p, f = calc_cheapest_position(cgs)

    print(f'The cheapest position is: {p} with {f} fuel consumed.')

    print('2th part:')
    p, f = calc_cheapest_position(cgs, two=True)
    print(f'The cheapest position is: {p} with {f} fuel consumed.')

if __name__ == '__main__':
  main()