def main():
    consumption = int(input())
    price = 7
    if consumption > 10:
        price += (consumption - 10)
    if consumption > 30:
        price += (consumption - 30)
    if consumption > 100:
        price += (consumption - 100)*3
    print(price)

if __name__ == "__main__":
    main()