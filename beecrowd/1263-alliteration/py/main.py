def main():
    while True:
        try:
            alliteration = '#'
            words = input().split()
            for i in range(len(words)-1):
                if words[i][0].lower() == words[i+1][0].lower():
                    if words[i][0].lower() != alliteration[-1]:
                        alliteration += words[i][0].lower()
                else:
                    alliteration += '#'
            print(len(alliteration.replace('#', '')))
        except EOFError:
            break
if __name__ == "__main__":
    main()