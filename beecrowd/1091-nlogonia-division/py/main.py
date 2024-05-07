if __name__ == '__main__':
  while True:
    cases = int(input())

    if cases == 0:
      break
    
    x_division, y_division = map(int, input().split())
    for _ in range(cases):
      x, y = map(int, input().split())
      if x == x_division or y == y_division:
        print("divisa")
      elif x < x_division and y < y_division:
        print("SO")
      elif x > x_division and y < y_division:
        print("SE")
      elif x > x_division and y > y_division:
        print("NE")
      else:
        print("NO")
