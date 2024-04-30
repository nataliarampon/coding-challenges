if __name__ == "__main__":
  answer = input()
  correct_guesses = 0
  for guess in input().split():
    if guess == answer:
      correct_guesses += 1
  print(correct_guesses)