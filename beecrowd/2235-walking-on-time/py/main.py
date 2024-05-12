def main():
  credit_A, credit_B, credit_C = list(map(int, input().split()))
  if credit_A == credit_B or credit_A == credit_C or credit_B == credit_C:
    print('S')
  elif credit_A + credit_B == credit_C or credit_A + credit_C == credit_B or credit_B + credit_C == credit_A:
    print('S')
  else:
    print('N')                                                                                                                                                                                                                                                                                

if __name__ == '__main__':
  main()