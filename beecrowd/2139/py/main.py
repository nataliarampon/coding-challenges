from datetime import date

def main():
  YEAR = 2016
  christmas = date(YEAR, 12, 25)
  while True:
    try:
      month, day = map(int, input().split())

      diff = christmas - date(YEAR, month, day)
      if (diff.days < 0): 
        print('Ja passou!')
      elif (diff.days == 1):
        print('E vespera de natal!')
      elif (diff.days > 0):
        print(f'Faltam {diff.days} dias para o natal!')
      elif (diff.days == 0 ):
        print('E natal!')

    except EOFError:
      break

if __name__ == "__main__":
    main()