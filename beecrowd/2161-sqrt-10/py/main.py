def sqrt10(n):
  if n == 0:
    return 0
  return 1 / (6 + sqrt10(n-1)) 

def main():
  print(f'{3 + sqrt10(int(input())):.10f}')

if __name__ == "__main__":
  main()