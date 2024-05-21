def main():
  people_per_floor = []
  for _ in range(3):
    people_per_floor.append(int(input()))
  
  minutes = []
  for i in range(3):
    count = 0
    for j in range(3):
      count += 2*abs(i-j)*people_per_floor[j]
    minutes.append(count)
  print(min(minutes))

if __name__ == '__main__':
  main()