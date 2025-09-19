from datetime import date

def main():
  while True:
    cases = int(input())
    if cases == 0:
      break
    for _ in range(cases):
      people = int(input())
      orders = 2 * people - (2 if people % 2 == 0 else 1)
      print(orders)

if __name__ == "__main__":
    main()