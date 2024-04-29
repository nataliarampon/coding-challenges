class Solution(object):
  def isPalindrome(self, x):
    number_string = str(x)
    length = len(number_string)
    for i in range(length//2):
      if number_string[i] != number_string[length-i-1]:
        return False
    return True
    