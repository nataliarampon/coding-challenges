def main():
  length = int(input())
  odd = []
  even = []
  for _ in range(length):
    n = int(input())
    if n % 2 == 0:
      even.append(n)
    else:
      odd.append(n)
  even.sort()
  odd.sort(reverse=True)

  for n in (even + odd):
    print(n)

if __name__ == '__main__':
  main()