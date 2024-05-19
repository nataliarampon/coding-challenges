def main():
  length = int(input())
  measures = list(map(int, input().split()))
  decrease = 0
  for i in range(1, length):
    if (measures[i] < measures[i-1]) and decrease == 0:
      decrease = i + 1
  print(decrease)

if __name__ == '__main__':
  main()