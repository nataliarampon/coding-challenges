def main():
  while True:
    try:
      nb_citizens, queries = map(int, input().split())
      citizens = []
      for _ in range(nb_citizens):
        citizens.append(int(input()))
      citizens.sort(reverse=True)
      for _ in range(queries):
        query = int(input())
        print(citizens[query - 1])
    except EOFError:
      break

if __name__ == "__main__":
  main()