# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


"""
### NOTES ###
    1. L and R pointers
    2. when they aren't equal, increment L and set its value to [R]
    3. return L + 1
""" 


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l+=1
                nums[l] = nums[r]
        return l+1