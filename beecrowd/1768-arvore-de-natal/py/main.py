def main():
    while True:
        try:
            n = int(input())
            for i in range(1,n+1,2):
                print(f"{((n-i)//2)*' ' + i*'*'}")
            print(f"{(n//2)*' ' + '*'}")
            print(f"{((n//2)-1)*' ' + '***'}")
            print('')
        except EOFError:
            break    

if __name__ == "__main__":
    main()