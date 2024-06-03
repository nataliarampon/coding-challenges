def main():
    LIMIT_X = 432
    LIMIT_Y = 468

    x,y = map(int, input().split())
    if x >= 0 and x <= LIMIT_X and y >= 0 and y <= LIMIT_Y:
        print('dentro')
    else:
        print('fora')

if __name__ == "__main__":
    main()