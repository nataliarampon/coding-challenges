import math

def euclidean_distance(point1, point2):
    return math.sqrt(abs(point2[0] - point1[0]) ** 2 + abs(point2[1] - point1[1]) ** 2)

def main():
  while True:
    try:
      radius_hunter, x_hunter, y_hunter, radius_flower, x_flower, y_flower = map(int, input().split())
      centers_distance = euclidean_distance((x_hunter, y_hunter), (x_flower, y_flower))
      if (centers_distance + radius_flower) > radius_hunter:
        print('MORTO')
      else:
        print('RICO')
    except EOFError:
      break

if __name__ == "__main__":
  main()