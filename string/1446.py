# 1446. Consecutive Characters
# https://leetcode.com/problems/consecutive-characters/


"""
### NOTES ###
    1. set count of 1
    2. set pointer to index 1
    3. loop and check if [i] == [i-1]
        a. if equal --> count += 1
        b. otherwise --> reset count to 1
        c. track the max_count in each loop
""" 


class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count, count)
        return max_count