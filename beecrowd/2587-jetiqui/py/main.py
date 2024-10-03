def main():
  for _ in range(int(input())):
    first_option = input()
    second_option = input()
    state = input()

    matches_indexes = [i for i, char in enumerate(state) if char == '_']
    if first_option[matches_indexes[0]] == second_option[matches_indexes[1]] \
       or first_option[matches_indexes[1]] == second_option[matches_indexes[0]]:
      print('Y')
    else:
      print('N')

if __name__ == "__main__":
  main()