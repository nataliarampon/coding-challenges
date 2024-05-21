def main():
  GRADE_THRESHOLD = 8

  cases = int(input())

  max_grade = 0
  max_student = ''
  for _ in range(cases):
    student, grade = input().split()
    grade = float(grade)
    if grade > max_grade:
      max_grade = grade
      max_student = student

  if max_grade >= GRADE_THRESHOLD:
    print(max_student)
  else:
    print('Minimum note not reached')

if __name__ == '__main__':
  main()