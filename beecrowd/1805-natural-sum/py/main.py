def main():
  start, finish = map(int, input().split())
  n = finish - start + 1
  sum = (start+finish)*n//2
  print(sum)

if __name__ == '__main__':
  main()