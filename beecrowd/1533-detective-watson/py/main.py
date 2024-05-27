def main():
  while True:
    n = int(input())
    if n == 0:
      break
    suspects = list(map(int, input().split()))
    sorted_suspects = sorted(suspects)
    print(suspects.index(sorted_suspects[-2])+1)

if __name__ == "__main__":
  main()