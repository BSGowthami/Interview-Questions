"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

#push all open brackets and when a closed bracket is seen, pop from stack and check if its corresponding open bracket.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        stack = []
        
        for x in s:
            if x in ['(', '{', '[']:
                stack.append( x )
            else:
                if len( stack ) == 0:
                    return False
                if ( x == ')' and stack[-1] == '(' ) or ( x == '}' and stack[-1] == '{' ) or ( x == ']' and stack[-1] == '[' ):
                    del stack[-1]
                else:
                    return False
        #if all parenthesis are coevred and stack is not empty, its unbalanced
        if len(stack) == 0:
            return True
        else:
            return False
