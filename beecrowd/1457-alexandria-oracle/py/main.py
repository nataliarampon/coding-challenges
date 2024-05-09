if __name__ == '__main__':
  cases = int(input())
  for _ in range(cases):
    factorial_string = input()
    k = factorial_string.count('!')
    n = int(factorial_string.split(sep='!')[0])

    result = 1
    i = 0
    while n - k*i > 1:
      result *=  n - k*i
      i += 1
    
    print(result)