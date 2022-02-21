class Result:
  self.winner_board
  self.last_number
  self.sum_unmarket_numbs

def bingo_game(numbers, boards):
  pass



def extract_numbers(raw_lines):
  numbers = raw_lines[0].split(',')
  numbers = [ int(n) for n in numbers ]  

  return numbers

def extract_boards(raw_lines):
  boards = []
  for i in range(2, len(raw_lines), 6):
    board = []
    for j in range(i, i+5):
      row = raw_lines[j].strip().replace('  ', ' ').split(' ')

      row = [ int(n) for n in row ]
      board.append(row)
    boards.append(board)

  return boards

def extract_input(raw_lines):
  numbers = extract_numbers(raw_lines)
  boards = extract_boards(raw_lines)    

  return numbers, boards

def main():
  with open("example.txt") as f:
    raw_lines = f.readlines()
    numbers, boards = extract_input(raw_lines)

    winner = bingo_game(numbers, boards)

if __name__ == '__main__':
  main()