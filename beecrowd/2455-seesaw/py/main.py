if __name__ == '__main__':
  person1, length1, person2, length2 = map(int, input().split())
  weight1 = person1 * length1
  weight2 = person2 * length2
  if weight1 < weight2:
    print(1)
  elif weight1 > weight2:
    print(-1)
  else:
    print(0)