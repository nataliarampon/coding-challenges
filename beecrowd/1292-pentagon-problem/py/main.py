import math

def main():
  CONVERSION = math.cos(math.pi/20) + math.tan(3*math.pi/20)*math.sin(math.pi/20)
  while True:
    try:
      pentagon_side = float(input())
      print(f'{pentagon_side*CONVERSION:.10f}')
    except EOFError:
      break

if __name__ == '__main__':
  main()