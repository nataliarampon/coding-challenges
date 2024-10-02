def main():
  numbers = map(int, input().split())
  largest = 0

  for n in numbers:
    if n == 0:
      break
    if n > largest:
      largest = n
  print(largest)

if __name__ == "__main__":
  main()