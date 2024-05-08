if __name__ == '__main__':
  NUMERIC_GRADE = 0
  LETTER_GRADE = 1

  num_to_letter_mapping = [(86, 'A'), (61, 'B'), (36, 'C'), (1, 'D'), (0, 'E')]
  numeric_grade = int(input())

  for i in range(len(num_to_letter_mapping)):
    if numeric_grade >= num_to_letter_mapping[i][NUMERIC_GRADE]:
      print(num_to_letter_mapping[i][LETTER_GRADE])
      break