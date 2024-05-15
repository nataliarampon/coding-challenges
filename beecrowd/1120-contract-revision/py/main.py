def main():
  while True:
    digit, number = input().split()
    if digit == '0' and number == '0':
      break
    contract_value = number.replace(digit, '')
    print(0 if contract_value == '' else int(contract_value))

if __name__ == '__main__':
  main()