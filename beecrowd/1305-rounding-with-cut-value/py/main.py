def main():
    while True:
        try:
            num = float(input())
            cutoff = float(input()) % 1
            print(int((num // 1) + (1 if num % 1 > cutoff else 0)))
        except EOFError:
            break

if __name__ == "__main__":
    main()