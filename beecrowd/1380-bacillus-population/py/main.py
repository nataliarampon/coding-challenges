PISANO_PERIOD_MOD_1K = 1500

def int_mod(s):
  acc = 0
  for char in s:
    acc = (acc * 10 + int(char)) % PISANO_PERIOD_MOD_1K
  return acc

def main():
  memoization  = { 0: 0, 1: 1 }

  cases = int(input())
  for _ in range(cases):
    k = int_mod(input())

    for i in range(2, k + 1):
      if i not in memoization:
        memoization[i] = (memoization[i-1] + memoization[i-2]) % 1000
    print(f'{memoization[k]:03d}')

if __name__ == '__main__':
  main()