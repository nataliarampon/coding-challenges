from functools import reduce

MATRING_SIZE = 4
matring = []

def getColumnNumber(index):
  return int(reduce(lambda x,y : x + y, [matring[i][index] for i in range(MATRING_SIZE)]))

def main():
  for _ in range(MATRING_SIZE):
    matring.append(input())
  first_value = getColumnNumber(0)
  last_value = getColumnNumber(-1)

  res = ''
  for i in range(1,len(matring[0]) - 1):
    res += chr((first_value*getColumnNumber(i) + last_value) % 257)
  print(res)

if __name__ == "__main__":
  main()