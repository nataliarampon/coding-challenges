def main():
    while True:
        try:
            dna = input()
            resistence = input()
            if resistence in dna:
                print('Resistente')
            else:
                print('Nao resistente')
        except EOFError:
            break 

if __name__ == "__main__":
    main()