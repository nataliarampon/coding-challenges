def main():
  n = int(input())

  for _ in range(n):
    password = input()
    variations = 1
    for c in password:
      if c in 'AaEeIiOoSs':
        variations *= 3
      else:
        variations *= 2
    print(variations)

if __name__ == '__main__':
  main()