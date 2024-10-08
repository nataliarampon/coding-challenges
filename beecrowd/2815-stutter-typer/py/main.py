def main():
    words = input().split()
    corrected_words = []
    for word in words:
        if word[:2] == word[2:4]:
          corrected_words.append(word[2:])
        else:
          corrected_words.append(word)
    print(' '.join(corrected_words))

if __name__ == "__main__":
    main()