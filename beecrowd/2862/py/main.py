def main():
  cases = int(input())
  for _ in range(cases):
    print('Inseto!' if int(input()) <= 8000 else 'Mais de 8000!')

if __name__ == "__main__":
  main()