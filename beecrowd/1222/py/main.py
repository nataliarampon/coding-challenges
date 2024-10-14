def main():
    SPACE = 1
    while True:
        try:
            _, lines_per_page, chars_per_line = map(int, input().split())
            words = input().split()
            pages = 1
            current_line_chars = 0
            current_page_lines = 0
            for w in words:
                if (current_line_chars + len(w)) <= chars_per_line:
                    current_line_chars += len(w) + SPACE
                else:
                    current_line_chars = len(w) + SPACE
                    current_page_lines += 1

                if current_page_lines == lines_per_page:
                    current_page_lines = 0
                    pages += 1 
            print(pages)
        except EOFError:
            break

if __name__ == "__main__":
    main()