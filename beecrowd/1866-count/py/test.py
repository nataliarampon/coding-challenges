import unittest
from main import calculateSequence

class TestSequenceCount(unittest.TestCase):
  
  def test_odd_sequence(self):
    self.assertEqual(1, calculateSequence(7))
    self.assertEqual(1, calculateSequence(11))
  
  def test_even_sequence(self):
    self.assertEqual(0, calculateSequence(18))

if __name__ == "__main__":
  unittest.main()
