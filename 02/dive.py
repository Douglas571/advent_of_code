class Command:
  def __init__(self, name, amount):
    self.name = name
    self.amount = int(amount)

  def __str__(self):
    return f'name: {self.name}, amount: {self.amount}'

def calc_course(commands):
  depth = 0
  horizontal_pos = 0

  for cmd in commands:
    match cmd.name:
      case 'forward':
        horizontal_pos += cmd.amount

      case 'up':
        depth -= cmd.amount 

      case 'down':
        depth += cmd.amount

  return horizontal_pos, depth

def calc_course_2(commands):
  aim = 0
  depth = 0
  horizontal_pos = 0

  for cmd in commands:
    match cmd.name:
      case 'forward':
        horizontal_pos += cmd.amount
        depth += aim * cmd.amount

      case 'up':
        aim -= cmd.amount 

      case 'down':
        aim += cmd.amount

  return horizontal_pos, depth

def main():
  with open('input.txt') as f:
    commands = []
    for raw in f.readlines():
      name, amount = raw.split(' ')
      cmd = Command(name, amount)
      commands.append(cmd)

    hp, d = calc_course_2(commands)
    print(f'the result of d*hp is: {d*hp}')

if __name__ == '__main__':
  main()