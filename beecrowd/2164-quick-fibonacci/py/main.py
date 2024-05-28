import math

def main():
  n = int(input())
  rootFive = math.sqrt(5)
  fib = (((1 + rootFive)/2)**n - ((1 - rootFive)/2)**n)/rootFive
  print(f'{fib:.1f}')

if __name__ == "__main__":
  main()