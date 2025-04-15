def main():
  COUNTER_STRIKE = '0'
  while(True):
    try:
      cases, wanted_id = input().split()
      count = 0

      for _ in range(int(cases)):
        id, game = input().split()
        if id == wanted_id and game == COUNTER_STRIKE:
          count += 1
      print(count)
    except EOFError:
      break

if __name__ == "__main__":
  main()