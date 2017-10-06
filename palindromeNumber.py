"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        d = 1
        #To know the rounded range of x
        while x/d >= 10:
            d *= 10 
            
        #left and right digits of the number are compared
        #no exta space is used
        while x :
            left = x / d
            right = x % 10 
            if left != right:
                return False
            x = ( x % d ) / 10
            d /= 100
        return True
        
