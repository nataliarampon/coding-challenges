# Use of stdin cause it's faster than input()
from sys import stdin

def main():
    for case in range(int(stdin.readline())):
        if case != 0:
            print('')
        table = {}
        hash, _ = map(int, stdin.readline().split())
        addresses = list(map(int, stdin.readline().split()))
        for i in range(hash):
            table[i] = []
        for n in addresses:
            table[n % hash].append(str(n))
        for k in table.keys():
            print(f"{k}{' -> ' if table[k] != [] else ''}{' -> '.join(table[k])} -> \\")

if __name__ == "__main__":
    main()