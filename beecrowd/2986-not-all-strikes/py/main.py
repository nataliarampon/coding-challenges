
# time complexity too high with recursion
def getPossibilites(n):
  if n <= 1:
    return 1
  
  if n == 2:
    return 2

  return getPossibilites(n-1) + getPossibilites(n-2) + getPossibilites(n-3)

def main():
  steps = int(input())
  
  print(getPossibilites(steps))

if __name__ == "__main__":
  main()