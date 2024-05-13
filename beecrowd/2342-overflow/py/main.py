import re

def main():
  limit = int(input())
  matches = re.findall('(\d+) (\*|\+) (\d+)', input())[0]
  res = int(matches[0]) + int(matches[2]) if matches[1] == '+' else int(matches[0]) * int(matches[2])
  if res <= limit:
    print('OK')
  else:
    print('OVERFLOW')

if __name__ == '__main__':
  main()