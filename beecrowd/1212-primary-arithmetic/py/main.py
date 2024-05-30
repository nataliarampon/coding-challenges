def main():
  while True:
    num1, num2 = input().split()
    if num1 == '0' and num2 == '0':
      break
    
    total_carries = 0
    carry = 0
    for i in range(min(len(num1), len(num2))):
      if int(num1[-i-1]) + int(num2[-i-1]) + carry >= 10:
        carry = 1
        total_carries += 1
      else:
        carry = 0

    if len(num1) > len(num2) and int(num1[-i-2]) + carry >= 10:
        total_carries += 1
    if len(num2) > len(num1) and int(num2[-i-2]) + carry >= 10:
        total_carries += 1

    if total_carries == 0:
      print('No carry operation.')
    else:
      print(f'{total_carries} carry operation{"" if total_carries == 1 else "s"}.')

if __name__ == "__main__":
  main()