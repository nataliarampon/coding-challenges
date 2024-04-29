if __name__ == "__main__":
  weights = [300, 1500, 600, 1000, 150]
  sum = 225
  for i in range(5):
    weights[i] *= int(input())
    sum += weights[i]
  print(sum)