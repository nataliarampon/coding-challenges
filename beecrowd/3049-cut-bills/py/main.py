def main():
  HEIGHT = 70
  WIDTH = 160
  FULL_AREA = HEIGHT*WIDTH

  base = int(input())
  top = int(input())

  area = (base+top)*HEIGHT//2

  if area == FULL_AREA//2 :
    print(0)
  elif area > FULL_AREA//2 :
    print(1)
  else:
    print(2)

if __name__ == '__main__':
  main()