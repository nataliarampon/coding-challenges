def main():
  for _ in range(int(input())):
    hour, minute, state = map(int, input().split())
    print(f'{hour:02d}:{minute:02d} - A porta {"abriu" if state else "fechou"}!')

if __name__ == '__main__':
  main()
