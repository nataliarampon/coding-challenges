import re

def main():
  cases = int(input())
  for _ in range(cases):
    matches = re.findall('h(a+)mek(a+)me', input())[0]
    a = (matches[0].count('a') * matches[1].count('a'))*'a'
    print(f'k{a}')

if __name__ == '__main__':
  main()