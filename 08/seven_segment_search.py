def extrat_digits(raw_lines):
  digits = []

  for line in raw_lines:
    entry = { "output": [], "input": [] }

    raw_input_digits = line.strip('\n').split(' | ')[0].split(' ')
    for d in raw_input_digits:
      entry["input"].append(str().join(sorted(d)))
    
    raw_output_digits = line.strip('\n').split(' | ')[1].split(' ')
    for d in raw_output_digits:
      entry["output"].append(str().join(sorted(d)))

    digits.append(entry)

  return digits

def get_four_output_digits(digits):
  fods = []
  for row in digits:
    fods.append(row['output'])

  return fods

def count_unique_pattern_numbers(rows_of_digits):
  count = 0

  for row in rows_of_digits:
    for d in row:
        if len(d) in [2, 3, 4, 7]:
          count += 1

  return count 

def get_unique_pattern_digits(entry):
  decoded_digits = {}

  for d in entry['input']:
    number_of_segments = len(d)
    match(number_of_segments):
      case 2:
        decoded_digits[d] = '1'
        one = d
        
      case 3:
        decoded_digits[d] = '7'

      case 4:
        decoded_digits[d] = '4'
        four = d

      case 7:
        decoded_digits[d] = '8'

  return decoded_digits, one, four

def get_complex_digits(entry, one, four):
  decoded_digits = {}
  for d in entry['input']:
    number_of_segments = len(d)
    one = set(one)
    four = set(four)
    unknow = set(d)

    match(number_of_segments):
      case 5:
        one_rest = one - unknow
        four_rest = (four - one) - unknow

        if len(one_rest) == 0:
          decoded_digits[d] = '3'
        
        if len(four_rest) == 0:
          decoded_digits[d] = '5'

        if len(four_rest) == 1 and len(one_rest) == 1:
          decoded_digits[d] = '2'

      case 6:
        one_rest = one - unknow
        four_rest = (four - one) - unknow

        if len(one_rest) == 1:
          decoded_digits[d] = '6'

        if len(one_rest) == 0 and len(four_rest) == 1:
          decoded_digits[d] = '0'

        if len(one_rest) == 0 and len(four_rest) == 0:
          decoded_digits[d] = '9'

  return decoded_digits

def decode_digits(digits):
  res = []

  for entry in digits:
    decoded_digits = {}
    
    ( decoded_digits,
      one, 
      four ) = get_unique_pattern_digits(entry)
    complex_decodeds = get_complex_digits(entry, one, four)
    decoded_digits.update(complex_decodeds)

    entry['decoded_digits'] = decoded_digits
    entry['output_v'] = ''
    for d in entry['output']:
      entry['output_v'] += decoded_digits[d]

    res.append(entry)

  return res

def main():
  with open('input.txt') as f:
    digits = extrat_digits(f.readlines())
    fods = get_four_output_digits(digits)
    upn = count_unique_pattern_numbers(fods)
    print('--- Seven Segment Search ---')
    print('1th part:')
    print(f'the numbs of unique patters are: {upn}')

    print('2th part:')
    res = decode_digits(digits)
    sumatory = 0
    for entry in res:
      sumatory += int(entry['output_v'])
    print(f'the sum of all entries is: {sumatory}')

if __name__ == '__main__':
  main()