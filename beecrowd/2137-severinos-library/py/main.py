def main():
  while True:
    try:
      cases = int(input())
      books = []
      for _ in range(cases):
        books.append(input())
      books.sort()
      for book in books:
        print(book)
    except EOFError:
      break

if __name__ == '__main__':
  main()