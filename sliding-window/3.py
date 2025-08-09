# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


"""
### NOTES ###
    1. set 2 ptrs at beginning, init a hashset
    2. in loop check to see if [R] in set
        a. if so, keep remove from L and increment
        b. otherwise, add it to set and take max
""" 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        hashset = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])    
            max_substring = max(max_substring, len(hashset))
        return max_substring