import unittest
from main import Solution

class TestNumberPalindrome(unittest.TestCase):
  def setUp(self):
        self.classUnderTest = Solution()
  
  def test_negative_number(self):
    self.assertFalse(self.classUnderTest.isPalindrome(-121))
    self.assertFalse(self.classUnderTest.isPalindromeMath(-121))
    self.assertFalse(self.classUnderTest.isPalindromeMath(10))
  
  def test_palindrome_numbers(self):
    self.assertTrue(self.classUnderTest.isPalindrome(131))
    self.assertTrue(self.classUnderTest.isPalindrome(1661))
    self.assertTrue(self.classUnderTest.isPalindrome(0))
    self.assertTrue(self.classUnderTest.isPalindromeMath(131))
    self.assertTrue(self.classUnderTest.isPalindromeMath(1661))
    self.assertTrue(self.classUnderTest.isPalindromeMath(0))

if __name__ == "__main__":
  unittest.main()