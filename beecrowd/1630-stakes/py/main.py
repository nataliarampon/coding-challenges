from math import gcd

def main():
  while True:
    try:
      width, height = map(int, input().split())
      if width == height:
        print(4)
      else:
        divisor = gcd(width, height)
        print(2*(height + width)//divisor)
    
    except EOFError:
      break

if __name__ == "__main__":
  main()
