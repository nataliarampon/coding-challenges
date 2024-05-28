def main():
  age = []
  for _ in range(3):
    age.append(int(input()))
  age.append(age[0] - age[1] - age[2])
  age.sort(reverse=True)
  print(age[1])

if __name__ == "__main__":
  main()