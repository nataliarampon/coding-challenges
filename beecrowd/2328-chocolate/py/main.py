def main():
    _ = input()
    divisions = map(int, input().split())
    pieces = 0
    for d in divisions:
        pieces += d - 1
    print(pieces)

if __name__ == "__main__":
    main()