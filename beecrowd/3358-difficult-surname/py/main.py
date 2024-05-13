def isVowel(letter):
  VOWELS = 'aAeEiIoOuU'
  return letter in VOWELS

def isSurnameHard(surname):
  sequence_count = 0
  res = False
  for c in surname:
      if isVowel(c):
        sequence_count = 0
      else:
        sequence_count += 1
        if sequence_count == 3:
          res = True
          break
  return res

def main():
  n = int(input())

  for _ in range(n):
    surname = input()
    if isSurnameHard(surname): 
      print(f'{surname} nao eh facil')
    else:
      print(f'{surname} eh facil')
    

if __name__ == '__main__':
  main()