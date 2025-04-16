def main():
  distance, diameter1, diameter2 = map(int, input().split())
  print(f'{distance/(diameter1 + diameter2):.2f}')

if __name__ == "__main__":
  main()