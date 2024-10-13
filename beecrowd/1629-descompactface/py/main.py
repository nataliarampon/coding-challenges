def main():
    while True:
        cases = int(input())
        if cases == 0:
            break
        for _ in range(cases):
            n = input()
            bits = ''
            n_zeros = 0
            n_ones = 0
            for index, digit in enumerate(n):
                bits += int(digit) * f'{index % 2}'
                if index % 2:
                    n_ones += int(digit)
                else:
                    n_zeros += int(digit)
            verifier = 0
            for d in str(n_ones):
                verifier += int(d)
            for d in str(n_zeros):
                verifier += int(d)
            print(verifier)   

if __name__ == "__main__":
    main()