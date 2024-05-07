if __name__ == "__main__":
  CATEGORIES = [1,3,5,10,25,50,100]

  position = int(input())

  for i in range(len(CATEGORIES)):
    top_n = CATEGORIES[i]
    if position <= CATEGORIES[i]:
      break

  print('Top ' + str(top_n))