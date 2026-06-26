class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cnts, cntt = {}, {} # 2 empty dict to store character as key and its count as value

        # for frist string
        for char in s:
            if char in cnts:
                cnts[char] += 1
            else:
                cnts[char] = 1
        
        # for second string
        for char in t:
            if char in cntt:
                cntt[char] += 1
            else:
                cntt[char] = 1

        return cnts == cntt
        
