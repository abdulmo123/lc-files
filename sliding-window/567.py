# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/d


"""
### NOTES ###
    1. check if s1 bigger than s2 --> can't be permutation if so
    2. loop up to s1 len, freq map/arr for both s1 and s2
    3. loop thru remaining s2 chars:
        a. each iter.. add the [R]'s count to freq map/array
        b. drop the [L]'s count 
        c. check if freq map/arrays are equal
""" 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        l = 0
        for r in range(len(s1)):
            s1_count[ord(s1[r]) - ord('a')] +=1
            s2_count[ord(s2[r]) - ord('a')] +=1
        
        if s1_count == s2_count:
            return True
        
        for r in range(len(s1), len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[l]) - ord('a')] -= 1 
            l+=1

            if s1_count == s2_count:
                return True
        return False