from collections import Counter

def main():
  space_between_cases = False
  while True:
    try:
      line = input()
      if space_between_cases:
        print('')
      space_between_cases = True
      freq = Counter()
      for c in line:
        freq[ord(c)] += 1
      for char in sorted(freq.most_common(), key = lambda c : (c[1], -c[0])):
        print(f'{char[0]} {char[1]}')
      
    except EOFError:
      break
if __name__ == "__main__":
  main()
 