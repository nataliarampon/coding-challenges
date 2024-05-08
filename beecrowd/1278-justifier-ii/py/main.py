if __name__ == '__main__':
  space_between_cases = False
  while True:
    nb_lines = int(input())
    if nb_lines == 0:
      break

    if space_between_cases:
      print('')

    lines = []
    max_len = 0
    for i in range(nb_lines):
      lines.append(" ".join(input().split()))
      if len(lines[i]) > max_len:
        max_len = len(lines[i])
    
    for i in range(nb_lines):
      print(lines[i].rjust(max_len))
    space_between_cases = True