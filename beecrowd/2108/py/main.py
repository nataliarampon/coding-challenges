def main():
    biggest_word = ''
    while True:
        sentence = input()
        if sentence == '0':
            break
        words = sentence.split()
        words_size = []
        for w in words:
            if len(w) >= len(biggest_word):
                biggest_word = w
            words_size.append(str(len(w)))
        print('-'.join(words_size))
    print(f'\nThe biggest word: {biggest_word}')

if __name__ == "__main__":
    main()