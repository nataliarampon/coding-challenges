def main():
  cases = int(input())

  for _ in range(cases):
    name, _ = input().split()
    if name == 'Thor':
      print('Y')
    else:
      print('N')

if __name__ == '__main__':
  main()