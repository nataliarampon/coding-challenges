def main():
  cases = int(input())
  
  for _ in range(cases):
    n = int(input())
    # arithmetic sequence sum to the Nth number + 1
    print(((1 + n)*n)//2 + 1)

if __name__ == "__main__":
  main()