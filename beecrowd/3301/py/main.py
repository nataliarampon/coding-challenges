def main():
  ages = list(map(int, input().split()))
  
  if (ages[0] < ages[1] and ages[1] < ages[2]) or (ages[0] > ages[1] and ages[1] > ages[2]):
    print('zezinho')
  elif (ages[1] < ages[2] and ages[2] < ages[0]) or (ages[1] > ages[2] and ages[2] > ages[0]):
    print('luisinho')
  else:
    print('huguinho')

if __name__ == '__main__':
  main()