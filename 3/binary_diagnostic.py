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

  remainin_measures = []

  

  for i in range(msr_bit_len):
    for msr in report:
      bit = msr[i]

      if bit == '0':
        common_bits[i][0] += 1
      else:
        common_bits[i][1] += 1

    bit = common_bits[i]

    if bit[0] > bit[1]:
      for msr in report:
        remainin_measures = 

    else:
      remainin_measures = [ msr for msr in report if msr[i] == '1']

    print(f'{i}. {remainin_measures}') 

  return ogr, co2sr

def main():
  with open('input.txt') as f:
    measures = f.readlines()
    measures = [ msr.strip() for msr in measures]
    bgr, ber = binary_diagnostic(measures)

    gamma_rate = int(bgr, 2)
    epsilon_rate = int(ber, 2)

    pc = gamma_rate * epsilon_rate
    print(f'gamma_r: {gamma_rate}; epsilon_r: {epsilon_rate}')
    print(f'the power consuption is: {pc}')

if __name__ == '__main__':
  main()