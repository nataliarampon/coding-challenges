import math

def main():
  while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
      break
    volume = a * b * c
    print(f'{math.floor(volume**(1/3)):.0f}')

if __name__ == "__main__":
  main()