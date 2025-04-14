def main():
  message = input()
  print(message + ('0' if message.count('1') % 2 == 0 else '1'))

if __name__ == '__main__':
  main()