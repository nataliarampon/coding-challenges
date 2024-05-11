def main():
  line = int(input())
  column = int(input())

  if (line % 2 == 0 and column % 2 == 0) or (line % 2 != 0 and column % 2 != 0):
    print(1)
  else:
    print(0)

if __name__ == '__main__':
  main()