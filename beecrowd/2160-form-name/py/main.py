def main():
  MAX_LENGTH = 80
  message = input()
  print('YES' if len(message) <= MAX_LENGTH else 'NO')

if __name__ == '__main__':
  main()