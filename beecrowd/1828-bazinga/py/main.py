from enum import Enum

class Jokenpo(Enum):
  SCISSORS = 'tesoura'
  PAPER = 'papel'
  ROCK = 'pedra'
  LIZARD = 'lagarto'
  SPOCK = 'Spock'

winMapping = {
    Jokenpo.SCISSORS.value: [Jokenpo.PAPER.value, Jokenpo.LIZARD.value],
    Jokenpo.PAPER.value: [Jokenpo.ROCK.value, Jokenpo.SPOCK.value],
    Jokenpo.ROCK.value: [Jokenpo.LIZARD.value, Jokenpo.SCISSORS.value],
    Jokenpo.SPOCK.value: [Jokenpo.SCISSORS.value, Jokenpo.ROCK.value],
    Jokenpo.LIZARD.value: [Jokenpo.PAPER.value, Jokenpo.SPOCK.value]
  }

def simulateGame(firstPlayer, secondPlayer):
  if (secondPlayer in winMapping[firstPlayer]):
    return 'Bazinga!'
  elif (firstPlayer == secondPlayer):
    return 'De novo!'
  else:
    return 'Raj trapaceou!'

if __name__ == '__main__':
  nb_matches = int(input())
  for i in range(nb_matches):
    firstPlayer, secondPlayer = input().split(' ')
    print('Caso #{}: {}'.format(i+1, simulateGame(firstPlayer, secondPlayer)));
