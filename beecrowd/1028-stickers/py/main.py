from math import gcd

def main():
  cases = int(input())
  for _ in range(cases):
    stack_a, stack_b = map(int, input().split())
    print(gcd(stack_a, stack_b))

if __name__ == '__main__':
  main()