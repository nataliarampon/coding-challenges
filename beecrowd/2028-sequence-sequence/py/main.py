def main():
  count = 1
  while True:
    try:
      n = int(input())
      sequence = []
      for i in range(n + 1):
        sequence += ([i]*(i if i > 0 else 1))
      print(f'Caso {count}: {len(sequence)} numero{"s" if len(sequence) > 1 else ""}')
      print(' '.join(str(a) for a in sequence))
      print('')
      count += 1
    except EOFError:
      break

if __name__ == '__main__':
  main()