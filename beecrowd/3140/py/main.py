def main():
  insideBody = False
  while True:
    try:
      line = input()
      if '<body>' in line:
        insideBody = True
      elif '</body>' in line:
        insideBody = False
      elif insideBody == True:
        print(line)
    except EOFError:
      break

if __name__ == "__main__":
  main()