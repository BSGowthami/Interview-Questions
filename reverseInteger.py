"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 0
        
        #remove the sign
        if x < 0:
            x = x * -1
            signed = True
        else:
            signed = False
        
        #inserting each right end digit of x in y 
        while x:
            y = y*10 + x%10
            x = x / 10
            
        # if y overflows, return 0. So, compare it with maximum possible integer.
        # can take longlong in C
        if y > 2147483647:
            return 0
        
        #put back the sign
        if signed:
            return y * -1
        else:
            return y
