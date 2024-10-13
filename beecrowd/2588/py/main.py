from collections import Counter

def main():
    while True:
        try:
            has_odd = False
            palindrome = input()
            counter = Counter(palindrome)
            add_letter = 0
            for _, freq in counter.items():
                if freq % 2 == 1:
                    if has_odd:
                        add_letter += 1
                    else:
                        has_odd = True
            print(add_letter)
        except EOFError:
            break 

if __name__ == "__main__":
    main()