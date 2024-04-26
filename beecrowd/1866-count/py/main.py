def calculateSequence(nb_terms):
  return 0 if nb_terms % 2 == 0 else 1

if __name__ == '__main__':

    nb_inputs = int(input())
    for i in range(nb_inputs):
      nb_terms = int(input())
      print(calculateSequence(nb_terms))