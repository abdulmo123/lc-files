# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

"""
### NOTES ###
    1. set 2 ptrs at beginning
    2. while looping:
        a. if [r] != 1 --> move L to 1 in front of R
        b. check to see what the max consec is
""" 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = max_consec = 0

        for r in range(len(nums)):
            if nums[r] != 1:
                l = r + 1
            
            max_consec = max(max_consec, r - l + 1)
        return max_consec