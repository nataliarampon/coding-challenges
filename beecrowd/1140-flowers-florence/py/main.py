def main():
  while True:
    sentence = input().split()
    tautogram = True
    if len(sentence) == 1 and sentence[0] == '*':
      break

    letter = sentence[0][0].lower()
    for words in sentence:
      if words[0].lower() != letter:
        tautogram = False
    print('Y' if tautogram else 'N')

if __name__ == "__main__":
  main()