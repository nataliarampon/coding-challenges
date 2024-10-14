def main():
    INT_THRESHOLD = 2147483647
    while True:
        try:
            sentence = input()
            number = ''
            for c in sentence:
                if c.isdigit():
                    number += c
                elif c == 'l':
                    number += '1'
                elif c == 'o' or c == 'O':
                    number += '0'
                elif c.isalpha():
                    number = ''
                    break
            if not number.isdecimal() or int(number) > INT_THRESHOLD:
                print('error')
            else:
                print(int(number))
        except EOFError:
            break

if __name__ == "__main__":
    main()