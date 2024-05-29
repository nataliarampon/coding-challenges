def getDiagonals(n):
  return int(n*(n-3)/2)

def main():
  print(getDiagonals(int(input())))
      
if __name__ == "__main__":
  main()