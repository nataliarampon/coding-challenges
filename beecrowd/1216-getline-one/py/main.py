def main():
  total = 0
  n = 0
  while True:
    try:
      _ = input()
      total += int(input())
      n += 1
    except EOFError:
      break 
  print(f'{total/n:.1f}')

if __name__ == "__main__":
  main()