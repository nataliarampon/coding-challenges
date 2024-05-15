import math

def isPrime(n):
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def main():
  cases = int(input())
  for _ in range(cases):
    n = int(input())
    if isPrime(n):
      print('Prime')
    else:
      print('Not Prime')

if __name__ == '__main__':
  main()