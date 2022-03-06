def binary_diagnostic(report):
  common_bits = [[0, 0] for _ in range(len(report[0]))]
  gamma_rate = '0b'
  epsilon_rate = '0b'

  for msr in report:
    for i, bit in enumerate(msr):
      if bit == '0':
        common_bits[i][0] += 1
      else:
        common_bits[i][1] += 1

  for bits in common_bits:
    if bits[0] > bits[1]:
      gamma_rate += '0'
      epsilon_rate += '1'
    else:
      gamma_rate += '1'
      epsilon_rate += '0'

  return int(gamma_rate, 2), int(epsilon_rate, 2)

def binary_diagnostic_2(report):
  msr_bit_len = len(report[0])
  common_bits = [ [0, 1] for _ in range(len(report[0]))]
  ogr = '0b'
  co2sr = 'ob'

  remainin_common_measures = [ x for x in report ]
  remainin_uncommon_measures = [ x for x in report ]

  i = 0
  while len(remainin_common_measures) > 1:
    bits = [0, 0]
    for msr in remainin_common_measures:
      if msr[i] == '0':
        bits[0] += 1
      else:
        bits[1] += 1

    if bits[1] >= bits[0]:
      new_measures = [ msr for msr in remainin_common_measures if msr[i] == '1']
    else:
      new_measures = [ msr for msr in remainin_common_measures if msr[i] == '0']

    remainin_common_measures = new_measures
    i += 1

  # Filtering uncommon measures and searching for
  # CO2 scrubber rating
  i = 0
  while len(remainin_uncommon_measures) > 1:
    bits = [0, 0]
    for msr in remainin_uncommon_measures:
      if msr[i] == '0':
        bits[0] += 1
      else:
        bits[1] += 1

    if bits[1] >= bits[0]:
      new_measures = [ msr for msr in remainin_uncommon_measures if msr[i] == '0']
    else:
      new_measures = [ msr for msr in remainin_uncommon_measures if msr[i] == '1']

    remainin_uncommon_measures = new_measures
    i += 1

  ogr = remainin_common_measures[0]
  co2sr = remainin_uncommon_measures[0]

  return int(ogr, 2), int(co2sr, 2)

def main():
  with open('input.txt') as f:
    measures = f.readlines()
    measures = [ msr.strip() for msr in measures]
    gamma_rate, epsilon_rate = binary_diagnostic(measures)

    pc = gamma_rate * epsilon_rate
    print('1th Part: Ratings')
    print(f'  Gamma: {gamma_rate}')
    print(f'  Epsilon: {epsilon_rate}')
    print(f'  Power consuption: {pc}\n')

    (
      oxygen_generator_rating, 
      co2_scrubber_rating
    ) = binary_diagnostic_2(measures)

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print('2th Part: Ratings')
    print(f'  Oxygen generator: {oxygen_generator_rating}')
    print(f'  CO2 scrubber: {co2_scrubber_rating}')
    print(f'  Life Support: {life_support_rating}')

if __name__ == '__main__':
  main()