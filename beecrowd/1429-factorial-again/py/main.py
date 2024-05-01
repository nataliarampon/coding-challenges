import math

if __name__ == "__main__":
  while True:
    n = input()
    if n == '0':
      break
    factorial = 0
    length = len(n)
    for i in range(length):
      factorial += math.factorial(length - i) * int(n[i])
    print(factorial) 