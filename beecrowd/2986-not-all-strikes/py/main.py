# time complexity too high with recursion
def getPossibilites(n):
  if n <= 1:
    return 1
  
  if n == 2:
    return 2

  # tribonacci sequence
  return getPossibilites(n-1) + getPossibilites(n-2) + getPossibilites(n-3)

# dynamic programming approach
def getPossibilitesDP(n):
  memoization = [ 0 for _ in range(max(n+1, 3))]
  memoization[0] = memoization[1] = 1
  memoization[2] = 2

  for i in range(3, n+1):
    memoization[i] = (memoization[i-1] + memoization[i-2] + memoization[i-3])%(10**9+7)
  
  return memoization[n]

def main():
  steps = int(input())
  
  print(getPossibilitesDP(steps))

if __name__ == "__main__":
  main()