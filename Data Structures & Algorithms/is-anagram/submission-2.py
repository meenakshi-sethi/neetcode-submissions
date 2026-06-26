class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS, dictT = {}, {}

        for char in s:
            crr_cnt_s = dictS.get(char, 0)
            dictS[char] = crr_cnt_s + 1
        
        for char in t:
            crr_cnt_t = dictT.get(char, 0)
            dictT[char] = crr_cnt_t + 1

        return dictS == dictT 