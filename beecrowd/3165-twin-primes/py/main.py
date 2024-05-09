from math import sqrt

def isPrime(n):
  if n == 1:
    return True

  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def main():
  n = int(input())

  for i in range(n, 6, -1):
    # for numbers greater than or equal to 7, the number between two prime twins must be divisible by 6
    # so no need to test those who aren't
    if (i - 1) % 6 == 0:
      if (isPrime(i) and isPrime(i-2)):
        print("{} {}".format(i-2, i))
        break
  
  if (n < 7):
    for i in range(n,  n // 2 + 1, -1):
      if (isPrime(i) and isPrime(i-2)):
        print("{} {}".format(i-2, i))
        break

if __name__ == '__main__':
  main()