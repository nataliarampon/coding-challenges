import unittest
from main import isRobberReachable

class TestCoastGuard(unittest.TestCase):
  
  def test_positive_cases(self):
    self.assertTrue(isRobberReachable(5, 1, 12))
    self.assertTrue(isRobberReachable(9, 12, 15))
  
  def test_negative_cases(self):
    self.assertFalse(isRobberReachable(12, 10, 7))
    self.assertFalse(isRobberReachable(12, 9, 10))
    self.assertFalse(isRobberReachable(10, 5, 5))

if __name__ == "__main__":
  unittest.main()
