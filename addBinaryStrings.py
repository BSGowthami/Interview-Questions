"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        
        #Adding two 0's has no carry and sum is 0
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary( a[0:-1], b[0:-1] ) + '0'
        #Adding two 1's gives 10 where 1 is carry
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary( self.addBinary( a[0:-1], b[0:-1] ), '1' ) + '0'
        #Adding 1, 0 or 0, 1 doesn't have carry as well 
        else:
            return self.addBinary( a[0:-1], b[0:-1] ) + '1'
                
