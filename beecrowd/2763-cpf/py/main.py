def main():
  cpf = input()

  split = cpf.split(sep='.')
  split += split[2].split(sep='-')
  split.pop(2)

  for part in split:
    print(part)

if __name__ == '__main__':
  main()