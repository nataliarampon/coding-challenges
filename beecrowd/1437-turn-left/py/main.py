def main():
  positions = 'NLSO'
  while True:
    n = int(input())
    if n == 0:
      break
    instructions = input()
    i = 0 
    for instruction in instructions:
      if instruction == 'E':
        i -= 1
      else:
        i += 1
    print(positions[i%len(positions)])  

if __name__ == "__main__":
  main()