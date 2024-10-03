def main():
  for _ in range(int(input())):
    start, end = map(int, input().split())
    res = ''
    for i in range(start,end+1):
      res += str(i)
    for i in range(len(res)-1, -1, -1):
      res += str(res[i])
    print(res)

if __name__ == "__main__":
  main()