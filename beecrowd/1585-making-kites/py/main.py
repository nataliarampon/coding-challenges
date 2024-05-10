def main():
  cases = int(input())
  
  for _ in range(cases):
    width, height = map(int, input().split())
    print('{} cm2'.format(width*height//2))

if __name__ == "__main__":
  main()