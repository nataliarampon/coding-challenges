def main():
  while True:
    try:
      last_upper = False
      sentence = input()
      dancing_sentence = ''
      for c in sentence:
        if last_upper and c.isalpha():
          dancing_sentence += c.lower()
          last_upper = not last_upper
        elif c.isalpha():
          dancing_sentence += c.upper()
          last_upper = not last_upper
        else:
          dancing_sentence += c
      print(dancing_sentence)
    except EOFError:
      break

if __name__ == '__main__':
  main()