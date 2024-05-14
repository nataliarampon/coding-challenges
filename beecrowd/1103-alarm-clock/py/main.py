def main():
  MINUTES_IN_HOUR = 60
  HOURS_IN_DAY = 24

  while True:
    hour_start, minute_start, hour_end, minute_end = map(int, input().split())
    if not (hour_start or minute_start or hour_end or minute_end):
      break
    if hour_end < hour_start:
      hour_end += HOURS_IN_DAY
    if hour_end == hour_start and minute_end < minute_start:
      hour_end += HOURS_IN_DAY

    print((hour_end - hour_start) * MINUTES_IN_HOUR + (minute_end - minute_start))

if __name__ == '__main__':
  main()