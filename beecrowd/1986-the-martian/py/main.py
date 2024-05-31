import math

def main():
  _ = input()
  msg = ''
  for hexa in input().split():
    msg += chr(int(hexa, 16))
  print(msg)

if __name__ == "__main__":
  main()