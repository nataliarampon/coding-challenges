import unittest
from main import simulateGame, Jokenpo

class TestBazingaGame(unittest.TestCase):
  
  def test_standard_jokenpo(self):
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.PAPER.value, Jokenpo.ROCK.value))
    self.assertEqual('Raj trapaceou!', simulateGame(Jokenpo.ROCK.value, Jokenpo.PAPER.value))
    self.assertEqual('De novo!', simulateGame(Jokenpo.PAPER.value, Jokenpo.PAPER.value))

  def test_winning_cases(self):
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.SCISSORS.value, Jokenpo.PAPER.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.PAPER.value, Jokenpo.ROCK.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.ROCK.value, Jokenpo.LIZARD.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.LIZARD.value, Jokenpo.SPOCK.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.SPOCK.value, Jokenpo.SCISSORS.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.SCISSORS.value, Jokenpo.LIZARD.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.LIZARD.value, Jokenpo.PAPER.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.PAPER.value, Jokenpo.SPOCK.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.SPOCK.value, Jokenpo.ROCK.value))
    self.assertEqual('Bazinga!', simulateGame(Jokenpo.ROCK.value, Jokenpo.SCISSORS.value))

if __name__ == '__main__':
  unittest.main()