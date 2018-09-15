from collections import Counter

def get_horizontal_pos(raw_lines):
  hp = [int(n) for n in raw_lines[0].split(',')]
  return hp

def get_cheapest_route(consuptions):
  cheapest = {
    'fuel': 0,
    'position': 0
  }

  for i, p in enumerate(consuptions):
    fuel = 0
    for crab in p:
      fuel += crab['fuel']

    print(f'fuel in {i} is: {fuel}')

    v = (fuel < cheapest['fuel'])
    print(f'fuel < cheapest["fuel"]: {v}')
    if v:
      print('here')
      cheapest['fuel'] = fuel
      cheapest['position'] = i

  print(cheapest)
  return cheapest['position'], cheapest['fuel']

def calc_cheapest_position(hp):
  total_pos = Counter()
  position = None
  fuel = None

  posible_pos = []

  for p in hp:
    total_pos[p] += 1

  largest = max([ int(n) for n, _ in total_pos.items()])

  consuption = []
  for i in range(largest):
    con = []
    for k, v in total_pos.items():
      fuel_consumed = abs(i-v)
      print(f'{k}:{v}')
      con.append({
        "start": int(k),
        "end": i,
        "fuel": fuel_consumed
      })
    consuption.append(con)

  print(total_pos)
  print(consuption[0])

  position, fule = get_cheapest_route(consuption)

  return position, fuel