from string import ascii_uppercase 

def getAlphabetPosition(char):
  return ascii_uppercase.index(char)

if __name__ == '__main__':
  cases = int(input())
  
  for _ in range(cases):
    lines = int(input())
    hash_value = 0 
    for i in range(lines):
      line = input()
      for j, char in enumerate(line):
        hash_value += getAlphabetPosition(char) + i + j
    print(hash_value)
