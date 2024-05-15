def main():
  HAPPY = ':)'
  SAD = ':('

  day_1, day_2, day_3 = map(int, input().split())
  if day_1 > day_2:
    if day_3 >= day_2:
      print(HAPPY)
    else:
      if abs(day_2 - day_3) >= abs(day_1 - day_2):
        print(SAD)
      else:
        print(HAPPY)
  elif day_1 < day_2:
    if day_3 <= day_2:
      print(SAD)
    else:
      if abs(day_3 - day_2) >= abs(day_2 - day_1):
        print(HAPPY)
      else:
        print(SAD)
  else:
    if day_3 > day_2:
      print(HAPPY)
    else:
      print(SAD)

if __name__ == '__main__':
  main()
