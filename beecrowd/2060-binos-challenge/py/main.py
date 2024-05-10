def main():
  multiples = { 2: 0, 3: 0, 4: 0, 5: 0}

  int(input())
  numbers = list(map(int, input().split()))

  for n in numbers:
    for mult in multiples:
      if n % mult == 0:
        multiples[mult] += 1
  
  for mult in multiples:
    print('{} Multiplo(s) de {}'.format(multiples[mult], mult))

if __name__ == '__main__':
  main()
