def main():
  between_cases = False
  while True:
    try:
      year = int(input())
      if between_cases:  
        print('')
      isLeapYear = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
      isHuluculuFestival = year % 15 == 0
      isBulukuluFestival = isLeapYear and year % 55 == 0

      if isLeapYear:
        print('This is leap year.')
      if isHuluculuFestival:
        print('This is huluculu festival year.')
      if isBulukuluFestival:
        print('This is bulukulu festival year.')

      if not (isLeapYear or isHuluculuFestival or isBulukuluFestival):
        print('This is an ordinary year.') 
      between_cases = True
    except EOFError:
      break

if __name__ == "__main__":
  main()