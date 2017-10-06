"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numlist = {}
        #include elements of array and their indiecs
        for i in range( len( nums ) ):
            if nums[i] not in numlist:
                numlist[nums[i]] = [i]
            else:
                numlist[nums[i]].append( i )
        #for each key in dictionary, check if target - key is present in dictionary.
       
        for i in range( len( nums ) ):
            del numlist[nums[i]][0]   # To avoid the case of key being recounted. E.g. 4 + 4 = 8
            if target - nums[i] in numlist and numlist[target - nums[i]] != []:
                return [i, numlist[target - nums[i]][0] ]
        return None
