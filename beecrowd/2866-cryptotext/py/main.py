def main():
    for _ in range(int(input())):
        crypto = input()
        decrypted = ''
        for c in reversed(crypto):
            if c.islower():
                decrypted += c
        print(decrypted)

if __name__ == "__main__":
    main()