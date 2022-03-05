from smoke_basin import *

def main():
  with open('input.txt') as f:
    raw_lines = f.readlines()
    fm = get_floor_map(raw_lines)
    lwps = get_lowest_points(fm)
    rlvs = get_risk_levels(lwps)
    sum_rlvs = sum(rlvs)

    print('--- Day 9: Smoke Basin ---')
    print(f'1t part\n the sum of risk levels are: {sum_rlvs}')

if __name__ == '__main__':
  main()