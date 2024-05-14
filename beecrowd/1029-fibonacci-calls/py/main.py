def main():
  RESULT = 0
  CALLS = 1

  memoization = { 0: (0,1), 1: (1, 1)}
  cases = int(input())
  for _ in range(cases):
    n = int(input())
    for i in range(2, n+1):
      memoization[i] = (memoization[i-1][RESULT] + memoization[i-2][RESULT], memoization[i-1][CALLS] + memoization[i-2][CALLS] + 1)
  
    print(f'fib({n}) = {memoization[i][CALLS] - 1} calls = {memoization[n][RESULT]}')

if __name__ == '__main__':
  main()