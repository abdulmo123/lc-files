# 30. Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/


"""
### NOTES ###
    1. create window, size of words * size of each word in words, R
    2. freq map to get freqs of words
    3. each window, check substring [L:R]
        a. create a map from that window and see if it makes the freq map of words
        b. if so, append the begin index to our res array
""" 


from typing import Counter, List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        window = n * len(words)
        res = []
        frequency_map = Counter(words)

        r = window
        l = 0

        for r in range(window, len(s)):
            if self.has_concat(s[l:r], n, frequency_map):
                res.append(l)
            l+=1
        
        if self.has_concat(s[l:r+1], n, frequency_map):
            res.append(l)

        return res

    def has_concat(self, string, n, frequency_map):
        seen = []
        for i in range(0, len(string), n):
            seen.append(string[i:i+n])
        return Counter(seen) == frequency_map 