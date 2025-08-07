# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/


"""
### NOTES ###
    1. set 2 ptrs at beginning, sub and max sub vals to 0
    2. at each iteration check:
        a. if the sub > sub + nums[r] -- if adding the next val increases the sum
            - set sub sub sum to nums[r], move left pointer up to right one 
        b. else --> add nums[r] to your sub sum value
        c. take the max between max_sub and sub
""" 


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        sub = 0
        max_sub = float("-inf")
        
        for r in range(len(nums)):
            if nums[r] > sub + nums[r]:
                sub = nums[r] 
                l = r
            else:
                sub += nums[r]

            max_sub = max(max_sub, sub)
        return max_sub 