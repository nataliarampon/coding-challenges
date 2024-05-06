def getFraction(n):
  if n == 0:
    return 0
  return 1/(2 + getFraction(n-1))

if __name__ == "__main__":
  n = int(input())
  result = 1
  result += getFraction(n)
  print("{:.10f}".format(result))