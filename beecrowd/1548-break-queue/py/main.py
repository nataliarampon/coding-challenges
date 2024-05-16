def main():
  cases = int(input())
  for _ in range(cases):
    n = int(input())
    students = list(map(int, input().split()))
    sortedStudents = sorted(students, reverse=True)

    unchanged = 0
    for i in range(n):
      if students[i] == sortedStudents[i]:
        unchanged += 1
    print(unchanged)

if __name__ == '__main__':
  main()