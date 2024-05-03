if __name__ == "__main__":
  sequence_length = int(input())
  new_sequence_length = []
  for i in range(sequence_length):
    n = input()
    if i == 0 or n != new_sequence_length[-1]:
      new_sequence_length.append(n)
  print(len(new_sequence_length))