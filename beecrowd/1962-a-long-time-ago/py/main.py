def main():
  YEAR = 2015
  for _ in range(int(input())):
    time = int(input())
    time = YEAR - time
    if time > 0:
      print(f'{time} D.C.')
    if time <= 0:
      print(f'{abs(time) + 1} A.C.')

if __name__ == '__main__':
  main()