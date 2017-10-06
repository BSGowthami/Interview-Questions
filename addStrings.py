"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    # Add digits with previous carry.
    def addChar(self, a, b, c0):
        c = 0
        s = int(a) + int(b) + int(c0)
        if s % 10 != s:
            c = s / 10
            s = s % 10
        return str(s), str(c)
        
    # Function to add two number strings
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len( num1 ) -1
        j = len( num2 ) -1
        summ = ""
        carry = '0'
        
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                s, c = self.addChar( num1[i], num2[j], carry )
                carry = c   # update carry
                summ = s + summ 
                i -= 1
                j -= 1
            elif i >= 0:
                s, c = self.addChar( num1[i], '0', carry )
                carry = c
                summ = s + summ
                i -= 1
            elif j >= 0: 
                s, c = self.addChar( '0', num2[j], carry )
                carry = c
                summ = s + summ
                j -= 1
        #Dont forget about the final carry
        if carry != '0':
            summ = carry + summ
        return summ
