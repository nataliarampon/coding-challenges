if __name__ == "__main__":
  days, balance = map(int, input().split())
  minimum = balance
  for _ in range(days):
    balance += int(input())
    if (balance < minimum):
      minimum = balance
  print(minimum)