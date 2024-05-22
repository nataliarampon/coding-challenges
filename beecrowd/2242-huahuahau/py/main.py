def isPalindrome(string):
  length = len(string)
  for i in range(length//2 + 1):
    if string[i] != string[length - i - 1]:
      return False
  return True

def main():
  VOWELS = 'aAeEiIoOuU'
  laughter = ''.join(c for c in input() if c in VOWELS)
  print('S' if isPalindrome(laughter) else 'N')

if __name__ == '__main__':
  main()