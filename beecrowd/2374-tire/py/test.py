import unittest
from main import getTirePressureDifference

class TestTirePressure(unittest.TestCase):
  
  def test_positive_difference(self):
    self.assertEqual(12, getTirePressureDifference(30,18))
  
  def test_negative_difference(self):
    self.assertEqual(0, getTirePressureDifference(27,27))
  
  def test_zero_difference(self):
    self.assertEqual(-3, getTirePressureDifference(27,30))
    

if __name__ == "__main__":
  unittest.main()
