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

def find_paths_2(g, start, end, path=[]):
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
  solution = len(paths)
  return solution
