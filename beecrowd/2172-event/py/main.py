if __name__ == "__main__":
  while True:
    x, exp = map(int, input().split())
    if x == 0 and exp == 0:
      break
    print(x*exp)