from string import ascii_lowercase

if __name__ == '__main__':
  count = 97
  i = 0
  while count <= 122:
    print("{} e {}".format(count, ascii_lowercase[i]))
    count += 1
    i += 1