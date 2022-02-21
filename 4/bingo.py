def bingo_game(numbers, boards):
  pass

def main():
  with open("example.txt") as f:
    data = f.readlines()

    numbers = data[0].split(',')
    numbers = [ int(n) for n in numbers ]
    print(numbers)

    print('--- boards ---')
    boards = []
    board = []
    for i, row in enumerate(data):
      if i == 0 or len(row.strip()) < 1: 
        continue

      if len(board) < 5:
        board.append(row)

      boards.append(row)
      
      board = []
      board.append(row)

    print(boards)

if __name__ == '__main__':
  main()