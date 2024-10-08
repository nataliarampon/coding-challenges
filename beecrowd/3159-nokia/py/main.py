keyboard = {
    'abc': '2',
    'def': '3',
    'ghi': '4',
    'jkl': '5',
    'mno': '6',
    'pqrs': '7',
    'tuv': '8',
    'wxyz': '9',
    ' ': '0'
}

def main():
    for _ in range(int(input())):
        res = ''
        last_key_used = ' '
        sentence = input()
        for c in sentence:
            was_upper = False
            if c.isupper():
                res += '#'
                c = c.lower()
                was_upper = True
            for key in keyboard:
                if c in key:
                    if last_key_used == key and not was_upper:
                        res += '*'
                    res += (key.index(c) + 1) * keyboard[key]
                    last_key_used = key
        print(res)         

if __name__ == "__main__":
    main()