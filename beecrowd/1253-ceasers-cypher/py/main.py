from string import ascii_uppercase

def main():
  cases = int(input())
  for _ in range(cases):
    encrypted = input()
    key = int(input())
    decrypted = ''
    for c in encrypted:
      decrypted += ascii_uppercase[ascii_uppercase.find(c) - key]
    print(decrypted)

if __name__ == '__main__':
  main()