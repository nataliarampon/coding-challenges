class Solution(object):
  def isPalindrome(self, x):
    number_string = str(x)
    length = len(number_string)
    for i in range(length//2):
      if number_string[i] != number_string[length-i-1]:
        return False
    return True
  
  def isPalindromeMath(self, x):
    if (x < 0):
      return False

    num = x
    reverse = 0
    
    while x > 0:
      last_digit = x % 10
      reverse = 10*reverse + last_digit
      x = x // 10
    
    return num == reverse