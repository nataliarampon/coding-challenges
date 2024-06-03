def main():
    case_count = 1
    while True:
        n = int(input())
        if n == 0:
            break
        nums = list(map(int, input().split()))
        for i in range(n):
            if nums[i] == i + 1:
                winner = i + 1
                break
        print(f'Teste {case_count}')
        print(winner)
        print('')
        case_count += 1

if __name__ == "__main__":
    main()