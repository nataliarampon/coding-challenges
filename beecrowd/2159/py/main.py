from math import log

def main():
  n = int(input())
  min = n / log(n)

  print(f'{min:.1f} {1.25506*min:.1f}')

if __name__ == "__main__":
  main()