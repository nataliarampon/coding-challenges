import re

def main():
  while True:
    try:
      FORMAT_REGEX = '(.+)\\+(.+)=(.+)'
      line = input()
      matches = re.findall(FORMAT_REGEX, line)[0]
      if matches[0].isalpha():
        print(int(matches[2]) - int(matches[1]))
      if matches[1].isalpha():
        print(int(matches[2]) - int(matches[0]))
      if matches[2].isalpha():
        print(int(matches[0]) + int(matches[1]))
    except EOFError:
      break
      
if __name__ == "__main__":
   main()