def main():
  num = list(map(int, input().split()))
  
  res = 'N'
  for i in range(len(num)-1):
    if res == 'N':
      if num[i] < num[i+1]:
        res = 'C'
      if num[i] > num[i+1]:
        res = 'D'
    if (res == 'C' and num[i] > num[i+1]) or (res == 'D' and num[i] < num[i+1]):
      res = 'N'
      break
  print(res)

if __name__ == "__main__":
  main()