def main():
  for _ in range(int(input())):
    diet = input()
    eaten = input() + input()

    cheater = False
    for food in eaten:
      if food not in diet:
        cheater = True
        break
      else:
        diet = diet.replace(food, '', 1)
    print('CHEATER' if cheater else ''.join(sorted(diet)))

if __name__ == "__main__":
  main()