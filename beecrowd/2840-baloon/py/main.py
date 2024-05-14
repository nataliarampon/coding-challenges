import math

def main():
  PI = 3.1415
  radius, total_gas = map(int, input().split())
  baloon_volume = 4/3 * PI * radius**3
  print(math.floor(total_gas/baloon_volume))

if __name__ == '__main__':
  main()