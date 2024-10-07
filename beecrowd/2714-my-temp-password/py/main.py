import re

def main():
  for _ in range(int(input())):
    ra = input()
    if (len(ra) != 20 or ra[:2] != 'RA'):
      print('INVALID DATA')
    else:
      print(int(ra[2:]))

if __name__ == "__main__":
  main()