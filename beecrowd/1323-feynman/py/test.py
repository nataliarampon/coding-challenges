import unittest
from main import calculateFeynman

class TestFeynmanSequence(unittest.TestCase):
  def test_stop_case(self):
    self.assertEqual(0, calculateFeynman(0))
  
  def test_sequence_cases(self):
    self.assertEqual(1, calculateFeynman(1))
    self.assertEqual(5, calculateFeynman(2))
    self.assertEqual(14, calculateFeynman(3))
    self.assertEqual(204, calculateFeynman(8))

if __name__ == '__main__':
  unittest.main()