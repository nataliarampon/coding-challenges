def main():
  NUMBER_EYES = 3
  OPEN_EYE = '*'

  count = 0
  while True:
    try:
      sentence = input()
      if sentence == 'caw caw':
        print(count)
        count = 0
      else:
        for i in range(NUMBER_EYES):
          if sentence[i] == OPEN_EYE:
            count += 2**(NUMBER_EYES - i - 1)

    except EOFError:
      break

if __name__ == '__main__':
  main()