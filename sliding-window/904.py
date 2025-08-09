# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/


"""
### NOTES ###
    1. problem asks: Find the longest continuous sub array that has exactly 2 distinct elements.
    2. as you slide, add the [R] to freq map
    3. when freq map size is greater than 2, elim all on the L until we are at size of 2 again
""" 

from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = float("-inf")
        l = 0
        hashmap = defaultdict(int)

        for r in range(len(fruits)):
            hashmap[fruits[r]] += 1
            print(len(hashmap))
            while len(hashmap) > 2:
                hashmap[fruits[l]] -=1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l+=1
            max_fruits = max(max_fruits, r-l+1)
        return max_fruits