def main():
  n = int(input())
  heights = list(map(int, input().split()))
  result = 1

  if n > 1 :
    for i in range(1,n):
      if heights[i] < heights[i-1] and (i == 1 or not is_last_valley):
        result = 1
      elif heights[i] > heights[i-1] and (i == 1 or is_last_valley):
        result = 1
      else:
        result = 0
        break
      is_last_valley = heights[i] < heights[i-1]

  print(result)

if __name__ == "__main__":
  main()