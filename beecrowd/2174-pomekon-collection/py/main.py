from collections import Counter

def main():
  TOTAL = 151
  count = Counter()
  for _ in range(int(input())):
    count[input()]+=1
  print(f'Falta(m) {TOTAL - len(count.keys())} pomekon(s).')

if __name__ == "__main__":
  main()