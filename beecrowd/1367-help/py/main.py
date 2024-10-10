def main():
    INCORRECT_PUNISHMENT = 20
    while True:
        n = int(input())
        if n == 0:
            break
        correct_test_cases = 0
        problem_times = {}
        correct_problems = []
        for _ in range(n):
            id, time, status = input().split()
            time = int(time)
            if id not in problem_times:
                problem_times[id] = 0
            if status == 'correct':
                correct_test_cases += 1
                problem_times[id] += time
                correct_problems.append(id)
            else:
                problem_times[id] += INCORRECT_PUNISHMENT
        total = 0
        for k in correct_problems:
            total += problem_times[k]
        print(f'{correct_test_cases} {total}')

if __name__ == "__main__":
    main()