def main():
  cases = int(input())
  for _ in range(cases):
    calc = input()
    result = int(calc[2:4]) + int(calc[5:8]) + int(calc[11:13])
    print(result)

if __name__ == '__main__':
  main()