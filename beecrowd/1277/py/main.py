def main():
    for _ in range(int(input())):
        n_students = int(input())
        student_names = input().split()
        student_attendance = input().split()
        banned_students = []
        for i in range(n_students):
            out = student_attendance[i].count('A')
            medic = student_attendance[i].count('M')
            leaves = out / (len(student_attendance[i]) - medic)
            if leaves > 0.25:
                banned_students.append(student_names[i])
        print(' '.join(banned_students))
if __name__ == "__main__":
    main()