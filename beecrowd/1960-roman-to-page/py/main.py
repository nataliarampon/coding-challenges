def main():
  mapping = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
  ]

  number = int(input())
  roman = ''
  while number != 0:
    for m in mapping:
      if number // m[0]:
        roman += m[1]
        number -= m[0]
        break
  print(roman)

if __name__ == '__main__':
  main()