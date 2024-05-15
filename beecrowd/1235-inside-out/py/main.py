def main():
  cases = int(input())
  for _ in range(cases):
    gibberish_sentence = input()
    m = len(gibberish_sentence)//2
    print(gibberish_sentence[m-1::-1] + gibberish_sentence[:m-1:-1])

if __name__ == '__main__':
  main()