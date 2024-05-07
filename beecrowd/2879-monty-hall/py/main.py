if __name__ == '__main__':
  n = int(input())
  wins = 0
  for _ in range(n):
    car_door = input()
    if car_door != '1':
      wins += 1
  print(wins)