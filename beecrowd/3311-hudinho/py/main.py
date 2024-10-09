def main():
    names_by_letter = {}
    for _ in range(int(input())):
        name = input()
        if name[0] in names_by_letter:
            names_by_letter[name[0]].append(name)
        else:
            names_by_letter[name[0]] = [name]
    
    for letter in sorted(names_by_letter.keys()):
        for name in names_by_letter[letter]:
            print(name)
    
if __name__ == "__main__":
    main()