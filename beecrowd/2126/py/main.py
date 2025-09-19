import re

def main():
  case_number = 1
  while True:
    try:
      print('\n' if case_number > 1 else '', end='')
      sub = input()
      sequence = input()

      pattern = '(?=' + re.escape(sub) + ')'
      matches = re.findall(pattern, sequence)
      subsequences = len(list(matches))
      last_subseq_pos = sequence.rfind(sub) + 1 if subsequences > 0 else -1

      print(f'Caso #{case_number}:')
      if last_subseq_pos == -1:
        print('Nao existe subsequencia')
      else:
        print(f'Qtd.Subsequencias: {subsequences}')
        print(f'Pos: {last_subseq_pos}')
      case_number += 1

    except EOFError:
      break

if __name__ == "__main__":
    main()