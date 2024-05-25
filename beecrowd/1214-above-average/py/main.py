def main():
  for _ in range(int(input())):
    grades = list(map(int, input().split()))[1:]
    average = sum(grades)/len(grades)
    above_avg = 0
    for grade in grades:
      if grade > average:
        above_avg += 1
    print(f'{100*above_avg/len(grades):.3f}%')

if __name__ == '__main__':
  main()