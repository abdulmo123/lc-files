# 15. 3Sum
# https://leetcode.com/problems/3sum/

"""
### NOTES ###
    1. sort array
    2. 1 loop for whole array, within that loop set ptrs at each end, i + 1 to len(nums) - 1
    3. when all thru ptrs sum = 0, add to result list
    4. skip over to avoid dups, at beginning skip where [i] == [i-1] and skip within j to k window where [j]] == [j-1]
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1            
        return res 