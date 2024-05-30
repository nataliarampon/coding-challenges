def main():
  for i in range(int(input())):
    num, base = input().split()
    print(f'Case {i+1}:')
    if base == 'bin':
      print(f'{int(num, 2)} dec')
      print(f'{int(num, 2):x} hex')
    if base == 'dec':
      print(f'{int(num, 10):x} hex')
      print(f'{int(num, 10):b} bin')
    if base == 'hex':
      print(f'{int(num, 16)} dec')
      print(f'{int(num, 16):b} bin')
    print('')

if __name__ == "__main__":
  main()