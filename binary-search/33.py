# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

"""
### NOTES ###
    1. binary search
    2. at each step, check which half is sorted:
        a. if nums[l] <= nums[m] --> left half is sorted
        b. else --> right half is sorted
    3. check if target is in the sorted half:
        a. if yes --> search that half
        b. if no --> search the other half
    4. repeat until found or pointers cross
""" 

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            
            if nums[m] == target:
                return m

            # left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right half is sorted
            else: 
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
        