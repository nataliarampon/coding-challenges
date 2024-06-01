def main():
  n, k = map(int, input().split())
  students = []
  for _ in range(n):
    students.append(input())
  students.sort()
  print(students[k-1])

if __name__ == "__main__":
  main()