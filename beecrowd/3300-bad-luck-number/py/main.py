def main():
    n = input()
    bad = False
    for i in range(len(n)-1):
        if n[i] == '1' and n[i+1] == '3':
            bad = True
            break
    print(f"{n}{'' if bad else ' NO'} es de Mala Suerte")

if __name__ == "__main__":
    main()