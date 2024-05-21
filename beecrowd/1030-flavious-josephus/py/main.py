def getSurvivor(remaining, n, k, i):
  kill = k - 1
  rounds = 0
  for i in range(n):
    if len(remaining) == 1:
      return remaining[0]
    else:
      rounds = kill // len(remaining) + 1
      killed = remaining.pop(kill%len(remaining))
      kill += k - rounds

def main():
  for i in range(int(input())):
    n, k = map(int, input().split())
    survivor = getSurvivor(list(range(1,n+1)), n, k, 0)
    print(f'Case {i + 1}: {survivor}')

if __name__ == '__main__':
  main()