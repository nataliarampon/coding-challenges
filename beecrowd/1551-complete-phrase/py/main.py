def main():
  SHIFT = ord('a')
  for _ in range(int(input())):
    phrase = input()
    alphabet = [False]*26
    for letter in phrase:
      if letter != ' ' and letter != ',':
        alphabet[ord(letter)-SHIFT] = True
    nb_letters = sum(alphabet)
    if nb_letters < 13:
      print('frase mal elaborada')
    elif nb_letters >= 13 and nb_letters < 26:
      print('frase quase completa')
    else:
      print('frase completa')

if __name__ == "__main__":
  main()