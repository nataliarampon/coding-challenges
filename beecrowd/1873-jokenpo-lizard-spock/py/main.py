def main():
  SCISSOR = 'tesoura'
  PAPER = 'papel'
  ROCK = 'pedra'
  LIZARD = 'lagarto'
  SPOCK = 'spock'

  for _ in range(int(input())):
    rajesh, sheldon = input().split()
    result = ''
    if rajesh == sheldon:
      result = 'empate'
    elif (rajesh == SCISSOR and (sheldon == PAPER or sheldon == LIZARD)) or \
    (rajesh == PAPER and (sheldon == ROCK or sheldon == SPOCK)) or \
    (rajesh == ROCK and (sheldon == LIZARD or sheldon == SCISSOR)) or \
    (rajesh == LIZARD and (sheldon == SPOCK or sheldon == PAPER)) or \
    (rajesh == SPOCK and (sheldon == PAPER or sheldon == SCISSOR)):
      result = 'rajesh'
    else:
      result = 'sheldon'
    print(result)

if __name__ == "__main__":
  main()