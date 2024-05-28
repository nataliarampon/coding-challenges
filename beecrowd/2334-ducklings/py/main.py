def main():
  while True:
    n = int(input())
    if n == -1:
      break
    print(n if n == 0 else n-1)

if __name__ == "__main__":
  main()