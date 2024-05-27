def main():
  while True:
    median, b = map(int, input().split())
    if median == 0 and b == 0:
      break
    print(2*median - b)

if __name__ == "__main__":
  main()