def main():
  clothes = int(input())
  min_wash, max_wash = map(int, input().split())
  min_dry, max_dry = map(int, input().split())

  if clothes >= min_wash and clothes >= min_dry \
    and clothes <= max_wash and clothes <= max_dry:
    print('possivel')
  else:
    print('impossivel')

if __name__ == '__main__':
  main()