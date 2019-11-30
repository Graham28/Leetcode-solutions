"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashset = {}
        
        for i in nums:
            hashset[i] = i
            
        for i in range(len(nums)):
            if (target - nums[i]) in hashset:
                #find target index
                for j in range(len(nums)):
                    if (nums[i] == target - nums[j]) & (i != j):
                        return [i, j]
                
                
                
                
             