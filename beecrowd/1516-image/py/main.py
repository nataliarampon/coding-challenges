def main():
    while True:
        original_height, original_width = map(int, input().split())
        if original_height == 0 and original_width == 0:
            break
        image = []
        for _ in range(original_height):
            image.append(input())
        target_height, target_width = map(int, input().split())

        new_image = []
        for i in range(original_height):
            new_line = ''
            for j in range(len(image[0])):
                new_line += (target_width//original_width) * image[i][j]
            for _ in range(target_height//original_height):
                new_image.append(new_line)

        for i in range(len(new_image)):
            print(new_image[i])
        print('')
if __name__ == "__main__":
    main()