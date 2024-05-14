def main():
  DAY_HOURS = 24
  departure, travel, timezone = map(int, input().split())
  print((departure + travel + timezone) % DAY_HOURS)

if __name__ == '__main__':
  main()