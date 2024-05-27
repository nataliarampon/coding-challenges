def main():
  for _ in range(int(input())):
    nb_languages = int(input())
    common_language = input()
    i = 1
    while i < nb_languages:
      i += 1
      if common_language != input():
        common_language = 'ingles'
    print(common_language)

if __name__ == "__main__":
  main()