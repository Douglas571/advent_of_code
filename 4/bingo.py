from collections import deque

def check_rows(board, market_numbers):
  for i, row in enumerate(board):
    if all(n in market_numbers for n in row):
      return row, i + 1

  return [], None

def check_cols(board, market_numbers):
  cols = [ [] for _ in range(len(board[0]))]
  for i, row in enumerate(board):
    for j, n in enumerate(row):
      cols[j].append(n)

  for i, col in enumerate(cols):
    if all(n in market_numbers for n in col):
      return col, i + 1

  return [], None

def get_unmarket_numbers(board, market_numbers):
  unmarket_numbers = []

  for row in board:
    for n in row:
      if not n in market_numbers:
        unmarket_numbers.append(n)

  return unmarket_numbers

def bingo_game(numbers, boards, market_numbers=None):
  market_numbers = market_numbers or []

  numbers = deque(numbers)
  result = { "winner": None }

  while not result["winner"]:
    n = numbers.popleft()
    market_numbers.append(n)

    for j, board in enumerate(boards):
      row, r = check_rows(board, market_numbers)
      col, c = check_cols(board, market_numbers)

      if r or c:
        unmarket_numbers = get_unmarket_numbers(board, market_numbers)
        sum_unmarket_numbers = sum(unmarket_numbers)

        score = sum_unmarket_numbers * n
        result = {
          "winner": j + 1,
          "last_number": n,
          "unmarked_numbers": unmarket_numbers,
          "sum_unmarked_numbers": sum_unmarket_numbers,
          "score": score
        }

        if col:
          result['completed_a'] = f'colum {c}'
          result['completed'] = col
        else:
          result['completed_a'] = f'row {r}'
          result['completed'] = row

  #print(market_numbers)
  #print(type(market_numbers))
  #for n in market_numbers:
    #print(n)
  return result

def trunkated_bingo_game(numbers, boards):
  numbers_copy = deque(numbers[:])
  market_numbers = []
  winners_ranking = []
  winners = []

  while len(numbers_copy) > 0:
    n = numbers_copy.popleft()
    market_numbers.append(n)

    for i, board in enumerate(boards):
      if i in winners: continue

      row, r = check_rows(board, market_numbers)
      col, c = check_cols(board, market_numbers)

      if r or c:
        winners.append(i)

        unmarket_numbers = get_unmarket_numbers(board, market_numbers)
        sum_unmarket_numbers = sum(unmarket_numbers)

        score = sum_unmarket_numbers * n

        winners_ranking.append(
          {
            "board": i+1,
            "score": score
          }
        )

  return winners_ranking

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
  with open("input.txt") as f:
    raw_lines = f.readlines()
    numbers, boards = extract_input(raw_lines)

    winner = bingo_game(numbers, boards)
    print('Results 1th part:')
    for k, v in winner.items():
      print(f'    {k}: {v}')

    winners = trunkated_bingo_game(numbers, boards)
    print('\nResults 2th part: trunkated')
    w = winners[-1]
    b = w['board']
    sc = w['score']
    print(f'the last winner is the board {b} with score of {sc}')
    
if __name__ == '__main__':
  main()