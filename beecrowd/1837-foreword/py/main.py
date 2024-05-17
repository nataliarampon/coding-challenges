def main():
  a, b = map(int, input().split())

  if a > 0 and b < 0:
    b *= -1
    q = (a//b) * -1
    r = a%b
  elif a < 0 and b < 0:
    a *= -1
    q = (a//b) * -1
    r = (a%b) * -1
  else:
    q = a//b
    r = a%b

  print(f'{q} {r}')


if __name__ == '__main__':
  main()