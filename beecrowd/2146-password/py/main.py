def main():
  while True:
    try:
      password = int(input())
      print(password - 1)
    except EOFError:
      break

if __name__ == '__main__':
  main()