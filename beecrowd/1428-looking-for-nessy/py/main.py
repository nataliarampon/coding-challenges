def main():
  for _ in range(int(input())):
    lines, cols = map(int, input().split())

    lines = lines - (1 if lines % 3 != 0 else 0)
    cols = cols - (1 if cols % 3 != 0 else 0)

    sonars = ((lines) // 3)*((cols) // 3)
    print(sonars)

if __name__ == "__main__":
  main()