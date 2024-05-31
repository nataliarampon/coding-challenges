def main():
  while True:
    n = int(input())
    if n == 0:
      break
    people = list(map(int, input().split()))
    total_time = 0
    for i in range(n):
      if i + 1 != n:
        total_time += min(people[i+1] - people[i], 10)
      else:
        total_time += 10
    print(total_time)

if __name__ == "__main__":
  main()