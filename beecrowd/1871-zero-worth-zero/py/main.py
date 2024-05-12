def main():
  while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
      break

    res = str(a + b).replace('0', '')
    print(res)                                                                                                                                                                                                                                                                          

if __name__ == '__main__':
  main()