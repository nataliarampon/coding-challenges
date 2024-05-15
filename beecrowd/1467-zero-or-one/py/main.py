def main():
  while True:
    try:
      a, b, c = map(int, input().split())
      if a == b == c:
        print('*')
      elif a == b:
        print('C')
      elif b == c:
        print('A')
      else:
        print('B')

    except EOFError:
      break

if __name__ == '__main__':
  main()