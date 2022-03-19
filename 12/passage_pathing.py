from collections import Counter

def print_g(g):
  print()
  for k in g:
    print(f'{k}: {g[k]}')
  print()

def get_input(raw_lines):
  graph = {}

  for l in raw_lines:
    a, b = l.strip('\n').split('-')

    if not a in graph.keys():
      graph[a] = []
      

    if not b in graph.keys():
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph


def explore(g, node, end, traveled):
  pass

"""
[
  {
    node: 'start',
    next: [
      { node: A, 
        next: [{node: 'end', next:[A]}]
      }
      { node: b,
        next: [{node: 'end', next:['A', 'b']}]}
    ]
  }
]
      -- A -- b --
start              end
      -- c -- d

[{node: start
  next: [
    {node:A, next: [{node:b, next:[{node:end, next:[]}]}]},
    {node:c, next: [{node:d, next:[]}]}

  ]
}]

tomar el primero
crear un temporar

copiar el primero n nodos siguientes
repetir el segundo
  
"""

def is_big_cave(c):
  return c.isupper()

def find_paths(g, start, end, path=[]):
  path = path + [start]

  if start == end:
    return [path]

  paths = []
  for node in g[start]:
    if not is_big_cave(node) and node in path: continue
  
    new_paths = find_paths(g, node, end, path)

    for new_path in new_paths:
      paths.append(new_path)

  return paths

def can_visite_cave(n, path, counter, visited_twice):
  if is_big_cave(n):
    return True

  # is small cave...
  if n == 'start': return False

  if visited_twice and counter[n] > 0: return False

  return True

def clone_counter(c):
  new_counter = Counter()

  for k, v in c.items():
    new_counter[k] = v

  return new_counter
  
def find_paths_2(g, start, end, path=[], counter=None, visited_twice=False):
  if not counter:
    counter = Counter()

  path = path + [start]
  counter[start] += 1

  if counter[start] == 2 and not is_big_cave(start):
      visited_twice = True

  if start == end:
    return [path]

  paths = []
  for node in g[start]:

    if not can_visite_cave(node, path, counter, visited_twice):
      # print(f'\ncut n={node}, path={path}\n  counter={counter}')
      continue

    new_paths = find_paths_2(g, node, end, path, clone_counter(counter), visited_twice)

    for new_path in new_paths:
      paths.append(new_path)

  return paths

def get_1th_solution(raw_lines):
  solution = 0

  gph = get_input(raw_lines)
  # print_g(gph)

  paths = find_paths(gph, 'start', 'end')
  # for path in paths:
  #   print(path)
  solution = len(paths)

  return solution

def get_2th_solution(raw_lines):
  solution = 0
  gph = get_input(raw_lines)
  paths = find_paths_2(gph, 'start', 'end')

  # for p in paths:
  #   print(p)

  solution = len(paths)
  return solution
