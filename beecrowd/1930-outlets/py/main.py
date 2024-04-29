from functools import reduce

if __name__ == "__main__":
  nb_outlets = reduce(lambda x,y : x + y, map(int, input().split())) - 3
  print(nb_outlets)