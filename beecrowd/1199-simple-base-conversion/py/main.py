def isHex(n):
  return n[1] == 'x'

def main():
  while True:
    n = input()
    if n[0] == '-':
      break
    elif len(n) == 1 or not isHex(n):
      print(f'0x{int(n):X}')
    else:
      print(int(n, 16))
      
if __name__ == "__main__":
  main()