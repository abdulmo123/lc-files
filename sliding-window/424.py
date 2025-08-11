# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/


"""
### NOTES ###
    1. set 2 ptrs at beginning, init a hashmap/dict
    2. in each iteration:
        a. have a max freq to be looking at the freq of curr char
        b. loop while bounds between R and L - max freq is greater than k
""" 


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = max_freq = res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -=1
                l+=1
            res = max(res, r - l + 1)
        return res