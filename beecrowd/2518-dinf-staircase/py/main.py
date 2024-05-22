import math

def main():
  CM_TO_M = 0.0001
  while True:
    try:
      steps = int(input())
      height, depth, length = map(int, input().split())
      surface = length * steps * math.sqrt(depth**2 + height**2)
      print(f'{surface*CM_TO_M:.4f}')

    except EOFError:
      break

if __name__ == '__main__':
  main()