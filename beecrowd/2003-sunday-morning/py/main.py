def main():
  LIMIT_TIME = 8
  COMMUTE_TIME = 1
  while True:
    try:
      hour, minute = map(int, input().split(sep=':'))
      late = 0
      if hour >= (LIMIT_TIME - COMMUTE_TIME):
        late = (hour + COMMUTE_TIME - LIMIT_TIME)*60 + minute
      print(f'Atraso maximo: {late}')

    except EOFError:
      break

if __name__ == '__main__':
  main()