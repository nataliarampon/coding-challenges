def main():
  while True:
    museums = int(input())
    if (museums == -1):
      break

    ticket_prices = list(map(int, input().split()))
    sum = 0
    visits = 0
    for ticket in ticket_prices:
      sum += ticket
      if (sum % 100 == 0):
        visits += 1
    print(visits)

if __name__ == "__main__":
  main()