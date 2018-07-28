'''
 Leetcode Problem#1 Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
# Sort List
# i from fisrt and go forward, j from last and go backward
# If i+j < target next i
# If i+j > target next j
# loop until i+j == target
# return index of i and j in original list
# if i == j find corresponding indices
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        i, j = 0, len(sorted_nums) - 1
        left, right = 0, 0
        found = False
        while not found:
            left = sorted_nums[i]
            right = sorted_nums[j]
            if left + right == target:
                found = True
            elif left + right < target:
                i = i + 1
            else:
                j = j - 1
        
        if left != right:
            i = nums.index(left)
            j = nums.index(right)
        else:
            i_list = [i for i,x in enumerate(nums) if x == left]
            i = i_list[0]
            j = i_list[1]
            
        return [i, j]
            
