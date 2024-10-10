def main():
    while True:
        try:
            sentence = ''.join(sorted(input().replace(' ','')))
            ranges = {}
            current_range = ''
            for i in range(len(sentence)):
                if i == 0 or (ord(sentence[i]) - ord(current_range[-1]) == 1 or ord(sentence[i]) - ord(current_range[-1]) == 0):
                    current_range += sentence[i]
                else:
                    ranges[current_range[0]] = current_range[-1]
                    current_range = sentence[i]
            if current_range:
                ranges[current_range[0]] = current_range[-1]
            res = ', '.join([f'{k}:{ranges[k]}' for k in ranges])
            print(res)
        except EOFError:
            break

if __name__ == "__main__":
    main()