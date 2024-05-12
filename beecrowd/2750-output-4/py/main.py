def main():
  print('-'*39)
  print('|  decimal  |  octal  |  Hexadecimal  |')
  print('-'*39)
  for i in range(16):
    print('|  {:^9}|{:^9}|{:^15}|'.format(i, oct(i)[2:], hex(i)[2:].upper()))
  print('-'*39)

if __name__ == '__main__':
  main()