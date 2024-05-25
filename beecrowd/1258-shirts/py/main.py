def main():
  between_cases = False
  while True:
    
    cases = int(input())
    if cases == 0:
      break
    if between_cases:
      print('')
    between_cases = True

    shirts = []
    for _ in range(cases):
      name =  input()
      color, size = input().split()
      shirts.append((color, size, name))
    
    shirts = sorted(shirts, key=lambda shirt: (shirt[0], -ord(shirt[1]), shirt[2]))
    for s in shirts:
      print(f'{s[0]} {s[1]} {s[2]}')

if __name__ == '__main__':
  main()
