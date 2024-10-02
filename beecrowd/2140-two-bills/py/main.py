BILLS = [2,5,10,20,50,100]
def isBillable(due):
  return due in BILLS

def isPossibleInTwoBills(due):
  for bill in BILLS:
    if due >= bill:
      if isBillable(due - bill):
        return True
  return False

def main():
  
  while True:
    cost, given = map(int, input().split())
    if cost == 0 and given == 0:
        break
    due = given - cost
    print('possible' if isPossibleInTwoBills(due) else 'impossible')

if __name__ == "__main__":
  main()