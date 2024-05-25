def main():
  broken = 0 
  for _ in range(int(input())):
    cans, glasses = map(int, input().split())
    if cans > glasses:
      broken += glasses
  print(broken)

if __name__ == '__main__':
  main()