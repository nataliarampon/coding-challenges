def main():
  while True:
    try:
      total, returned = map(int, input().split())
      missing = []
      nb_missing = total - returned
      tags = sorted(map(int, input().split()))
      i = 0
      count = 1

      while nb_missing != 0:
        if i >= len(tags) or tags[i] != count:
          missing.append(str(count))
          nb_missing -= 1
        else:
          i += 1
        count += 1

      if len(missing) > 0:
        print(' '.join(missing) + ' ')
      else:
        print('*')
    except EOFError:
      break

if __name__ == "__main__":
  main()