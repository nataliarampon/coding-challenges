def main():
  result = False
  sides = list(map(int, input().split()))

  for i in range(len(sides)):
    for j in range(i+1, len(sides)):
      for k in range(j+1, len(sides)):
        if sides[i] < sides[j] + sides[k] and \
        sides[j] < sides[i] + sides[k] and \
        sides[k] < sides[j] + sides[i]:
          result = True
  print('S' if result == True else 'N')
        

if __name__ == '__main__':
  main()