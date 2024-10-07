import re

def main():
  isFirst = True

  while True:
    nb_sentences = int(input())
    if nb_sentences == 0:
      break
    if not isFirst:
      print('') # Need a line only between test cases

    sentences = []
    max_len = 0
    for _ in range(nb_sentences):
      sentences.append(input())
      if len(sentences[-1]) > max_len:
        max_len = len(sentences[-1])
    for sentence in sentences:
      print(sentence.rjust(max_len))
    isFirst = False

if __name__ == "__main__":
  main()