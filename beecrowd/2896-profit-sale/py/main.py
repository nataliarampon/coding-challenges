def main():
  cases = int(input())
  for _ in range(cases):
    bought, empty_bottles_batch = map(int, input().split())
    print(bought // empty_bottles_batch + bought % empty_bottles_batch)

if __name__ == "__main__":
  main()