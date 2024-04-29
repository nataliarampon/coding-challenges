if __name__ == "__main__":
  readings = int(input())
  sum = 0
  for i in range(readings):
    time, speed = map(int, input().split())
    sum += time*speed
  print(sum)