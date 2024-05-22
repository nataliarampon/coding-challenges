def main():
  STR = 'x = 35'
  print('-'*39)
  print(f'|{STR:<37}|')
  print(f'|{"":<37}|')
  print(f'|{STR:^37}|')
  print(f'|{"":<37}|')
  print(f'|{STR:>37}|')
  print('-'*39)

if __name__ == '__main__':
  main()