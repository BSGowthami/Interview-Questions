"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #If initially there's only 1 digit in the number
        if num % 10 == num:
            return num
        add = 0
        while num > 0:
            add += num % 10 #adding each digit in the number
            num = num/10    #removing last digit (updating number)
        return self.addDigits(add) #recursion
