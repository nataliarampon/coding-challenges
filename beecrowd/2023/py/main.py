def main():
    names = []
    while True:
        try:
            name = input()
            names.append((name.lower(), name))
        except EOFError:
            break
    names = sorted(names, key= lambda e : e[0])
    print(names[-1][1])

if __name__ == "__main__":
    main()