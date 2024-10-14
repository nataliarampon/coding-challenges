def main():
    words = new_words = []
    _ = input()
    words = input().split()
    for word in words:
        if len(word) == 3 and (word[:2] == 'UR' or word[:2] == 'OB') and word[2] != 'I':
            word = word[:2] + 'I'
        new_words.append(word)
    print(' '.join(new_words))

if __name__ == "__main__":
    main()