from collections import Counter

def main():
  COUNT = 1

  for _ in range(int(input())):
    counter = Counter(c.lower() for c in input() if c.isalpha())
    max_count = counter.most_common()[0][COUNT]
    high_freq_letters = ''.join(sorted(letter[0] for letter in counter.most_common() if letter[COUNT] == max_count))
    print(high_freq_letters)

if __name__ == '__main__':
  main()