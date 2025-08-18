# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


"""
### NOTES ###
    1. check if p bigger than s --> can't be permutation if so
    2. loop up to p len, freq map/arr for both p and s
    3. loop thru remaining s chars:
        a. each iter.. add the [R]'s count to freq map/array
        b. drop the [L]'s count 
        c. check if freq map/arrays are equal --> if so append L to res array
""" 


from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []
        s_count = [0] * 26
        p_count = [0] * 26

        l = 0
        for r in range(len(p)):
            s_count[ord(s[r]) - ord('a')] += 1
            p_count[ord(p[r]) - ord('a')] += 1
        
        if s_count == p_count:
            res.append(l)

        for r in range(len(p), len(s)):
            s_count[ord(s[r]) - ord('a')] += 1
            s_count[ord(s[l]) - ord('a')] -= 1
            l+=1

            if s_count == p_count:
                res.append(l)
        return res