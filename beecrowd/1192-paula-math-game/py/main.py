def main():
  cases = int(input())
  for _ in range(cases):
    msg = input()
    digit1 = int(msg[0])
    digit2 = int(msg[2])
    op = msg[1]
    
    if digit1 == digit2:
      print(digit1*digit2)
    elif op.isupper():
      print(digit2 - digit1)
    else:
      print(digit2 + digit1)

if __name__ == '__main__':
  main()