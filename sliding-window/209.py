# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/


"""
### NOTES ###
    1. set 2 ptrs at beginning, init a total var to keep sum
    2. at each iteration check:
        a. add the at at R ptr
        b. while loop to see if total >= target
            - if so, take min between min_sub and distance between R and L ptrs
            - subtract items at L ptr as you increment it
""" 

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sub = float("inf")
        l = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_sub = min(min_sub, r-l+1)
                total -= nums[l]
                l+=1
        return min_sub if min_sub < float("inf") else 0